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


## Creer l contenair dans le repertoire ssh-ctf

cd ssh-ctf
docker build -t backup-ctf .

## Verification dial contenair

docker images

ghadi del9a wahid container isma backup-ctf


## Lancer le contenair avec le port ssh f 2222

docker run -d -p 2222:22 --name backup-ctf-machine backup-ctf


## Connexion SSH

Dans un autre terminal :

```bash
ssh guest@localhost -p 2222
password : guest@222
```
