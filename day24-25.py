# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:46:26 2025

@author: Triddles lamar
"""

import hashlib

def brute_force(target_hash, wordlist_path):
    with open(wordlist_path) as f:
        for word in f:
            if hashlib.sha256(word.strip().encode()).hexdigest() == target_hash:
                print(f"Password found: {word.strip()}") 
                return
    print("Password not found.")

# Example usage
target_hash = input("Enter target hash: ")
wordlist_path = input("Enter wordlist path: ")
brute_force(target_hash, wordlist_path)