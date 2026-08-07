#!/usr/bin/env python3
"""Seccomp Jail — real mini-challenge (seccomp-jail)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'openat-only')


def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as fh:
        fh.write(mat.get("delivery_blob", ""))
    os.makedirs("/challenge/secret", exist_ok=True)
    with open("/challenge/secret.key", "w") as fh:
        fh.write(f"{CHALLENGE_KEY}\n")
    with open("/challenge/jail.log", "w") as fh:
        fh.write("seccomp filter: execve blocked\n")
        fh.write("allowed: openat, read, write, exit\n")
        fh.write('shellcode path: openat(AT_FDCWD, "/challenge/secret.key", O_RDONLY)\n')
        fh.write(f"read() returned seed: {CHALLENGE_KEY}\n")
    print("Seccomp jail — openat /challenge/secret.key via allowed syscalls.")


if __name__ == "__main__":
    main()
