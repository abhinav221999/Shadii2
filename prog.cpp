#include <iostream>
#include <stdio.h>
#include "sqlite3.h"
#include <vector>
#include <map>
#include<string>

using namespace std;

vector<int> choose_prefs(vector<vector<int>> v1){
	map<int, int> mark;
	vector<int> a1;
	vector<int> a2;
	vector<int> a3;
	vector<int> rslt;
	for (int i=0; i < v1.size() ; i++){
		for (int j = 0; j < v1[i].size(); j++){
			mark[v1[i][j]] += 1;
		}
	}
	for (auto i : mark){
		if (i.second == 1)
			a1.push_back(i.first);
		else if (i.second == 2)
			a2.push_back(i.first);
		else
			a3.push_back(i.first);	
	}
	for (int i=0; i < a3.size(); i++){
		rslt.push_back(a3[i]);
	}
	for (int i=0; i < a2.size(); i++){
		rslt.push_back(a2[i]);
	}
	for (int i=0; i < a1.size(); i++){
		rslt.push_back(a1[i]);
	}
	a1.clear();
	a2.clear();
	a3.clear();
	mark.clear();
	return rslt;
}


int main(int argc, char const *argv[])
{
    char* err;
    sqlite3* db;
    sqlite3_stmt* profiles;
    sqlite3_stmt* interests;
    sqlite3_stmt* temp;
    sqlite3_stmt* existing;
	cout<<"something is here"<<"\n";
	sqlite3_open("db.sqlite3", &db);

	sqlite3_prepare_v2(db, "SELECT id FROM accounts_profile", -1, &profiles, 0);
	int profile, interest, count;
	vector<vector<int>> v1;
	vector<int> v2;
	vector<int> rslt;
	while (sqlite3_step(profiles) != SQLITE_DONE){
		profile = sqlite3_column_int(profiles, 0);
		cout << "profile = " << profile << "\n";
		string check_max = "SELECT COUNT() FROM accounts_profile_suggestions where profile_id = " + to_string(profile);
		sqlite3_prepare_v2(db, check_max.c_str(), -1, &existing, 0);
		sqlite3_step(existing);
		count = sqlite3_column_int(existing, 0);
		cout << "count = " << count << "\n";
		if (count < 50){
			string get_interests = "SELECT interest_id FROM accounts_profile_interests where profile_id = " + to_string(profile);
			sqlite3_prepare_v2(db, get_interests.c_str(), -1, &interests, 0);
			while (sqlite3_step(interests) != SQLITE_DONE){
				interest = sqlite3_column_int(interests, 0);
				cout << "interest = " << interest << "\n"; 
				string get_suggestions = "SELECT profile_id FROM accounts_profile_interests where interest_id = " + to_string(interest);
				sqlite3_prepare_v2(db, get_suggestions.c_str(), -1, &temp, 0);
				while (sqlite3_step(temp) != SQLITE_DONE){
					v2.push_back(sqlite3_column_int(temp, 0));
				}
				v1.push_back(v2);
				v2.clear();
			}
			rslt = choose_prefs(v1);
			for (int i= 0; i<rslt.size(); i++){
				if (profile != rslt[i]){
					string store_suggestion = "INSERT or IGNORE INTO accounts_profile_suggestions (profile_id, to_profile_id) VALUES (" + to_string(profile) + "," + to_string(rslt[i]) + ");";
					int rc = sqlite3_exec(db, store_suggestion.c_str(), NULL, NULL, &err);
					if (rc != SQLITE_OK){
			    	cout<<"Insert Error:"<<err;
					}
				}
			}
			v1.clear();
			}
	}
	sqlite3_close(db);
}