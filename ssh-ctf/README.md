# ========================================================


            Author : Ayoub EL MOUDEN


# ========================================================


# SSH Challenge

Had la machine ubuntu 9adha Hamid, walakin Hamid maki3refx f security mzian, o kis7ablih rasso bli la machine dialo bien securisé. 7awel d tbet bli Hamid ghalet.


Flag Format : ICODE{***}


Hint : Chof chnu tekdar t execute b root

## Credentials


Username: guest
Password: guest@222
SSH port: 2222


## Lancer le challenge

```bash
docker build --build-arg ROOT_FLAG="ICODE{flag}" -t backup_ssh_player_1
```

## Connexion SSH

Dans un autre terminal :

```bash
ssh ctfuser@localhost -p 2222
```

## Run The Instance

docker run -d -p 2222:22 --name player1 backup-ssh-player_1