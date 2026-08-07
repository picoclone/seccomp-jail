# Seccomp Jail (`seccomp-jail`)

**Category:** binary exploitation · **Difficulty:** hard · **Points:** 450

A seccomp filter blocks execve — use open/read/write shellcode to dump the seed.

## Run it

```bash
docker build -t picoclone/seccomp-jail .
# `picoclone start seccomp-jail` (or the web UI) prints the docker run line with your
# PICOCLONE_SERVER + PICOCLONE_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is Fernet ciphertext. Discover the key seed, derive the Fernet key, then decrypt.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
picoclone submit seccomp-jail 'picoclone{...}'
```

## Hints

- execve is filtered; enumerate which syscalls are allowed.
- openat + read + write is enough to exfiltrate the seed file.
