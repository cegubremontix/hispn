## How to decrypt the paswords

Usually in $HOME/.local/share/DBeaverData/..

https://stackoverflow.com/questions/39928401/recover-db-password-stored-in-my-dbeaver-connection

openssl aes-128-cbc -d \
  -K babb4a9f774ab853c96c2d653dfe544a \
  -iv 00000000000000000000000000000000 \
  -in credentials-config.json | \
  dd bs=1 skip=16 2>/dev/null
