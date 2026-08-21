---
title: 'Secure cluster connection'
summary: 'Learn the SSH concepts and connection habits used across managed research-computing systems.'
step: '01'
next_label: 'Next step'
next_title: 'Learn the cluster basics'
next_url: '/docs/commands/'
---

## SSH keys

Managed research-computing systems normally use SSH keys instead of passwords. A key pair has two parts: a public key that can be shared with the system and a private key that must remain on your own computer. Connection works only when the two keys match.

## Linux / mac

### Create a key pair

Run the following command in a terminal. The filename is a local label, so you can choose another clear name if you use it consistently.

```bash
ssh-keygen -t ed25519 -f research_cluster
```

The command creates `research_cluster`, the private key, and `research_cluster.pub`, the public key. Add a passphrase when prompted so that the private key is protected if your computer is lost or shared.

### Share the public key safely

Before connecting to a managed cluster, ask the **administrator of University** how public keys are accepted for that system. Share only the `.pub` file. Never share the private key, your passphrase, passwords, or access tokens.

Keep the private key in `~/.ssh/` with restricted permissions. A useful check is:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/research_cluster
```

### Build a reusable connection profile

Most SSH clients read connection profiles from `~/.ssh/config`. Replace the placeholders with the host name and user name provided for your own learning environment.

```text
Host research-cluster
    HostName CLUSTER_HOSTNAME
    User USER_NAME
    IdentityFile ~/.ssh/research_cluster
```

You can then connect with a short command:

```bash
ssh research-cluster
```

### Learn the access workflow

Every research-computing system has its own account, network, and authentication rules. Read the local access instructions supplied by your institution, then practise the sequence in a small test environment before transferring research data or starting a large job.

If the connection fails, record the exact command, the complete error message, and the point at which it occurs. This evidence is more useful than a screenshot alone when you review the problem or ask for help.

## Windows

### Create a key pair

Use an SSH client that can create and manage keys. Create an `ed25519` key pair, set a passphrase, and store the private key in a protected folder. The public key normally ends with `.pub`.

### Configure a connection

Enter the host name, user name, and private-key location supplied for your own system. Save the profile with a meaningful name such as `research-cluster`. Do not copy credentials from another learner or reuse a private key that belongs to someone else.

### Test deliberately

Make one connection attempt before moving files or launching software. Confirm the remote prompt, check your working directory with `pwd`, and exit cleanly with `exit`. This small practice loop helps you distinguish an access issue from a later software or scheduler problem.

## Connection learning checklist

1. Create one protected key pair.
2. Share only the public key through the local process.
3. Save a reusable profile with placeholders replaced.
4. Test one short SSH session.
5. Record the command and error text if something fails.

> **Safe practice rule:** never publish private SSH keys, passphrases, passwords, access tokens, participant information, or restricted research data.
