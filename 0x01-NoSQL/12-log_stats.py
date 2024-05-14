#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def main():
    """ main function"""
    client = MongoClient()
    db = client.logs
    logs = db.nginx
    num = logs.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    dic = {}
    for method in methods:
        dic[method] = logs.count_documents(filter={"method": method})
    print(f"{num} logs")
    print("Methods")
    for key, val in dic.items():
        print(f"\tmethod {key}: {val}")


if __name__ == "__main__":
    main()
