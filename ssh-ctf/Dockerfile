FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    openssh-server \
    sudo \
    nano \
    vim \
    netcat-openbsd \
    iproute2 \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Create SSH runtime directory
RUN mkdir /var/run/sshd

RUN printf "\n========================================\nAuthor : Ayoub EL MOUDEN\nMar7ba bik f l3amaria\n========================================\n\n" > /etc/motd

# Create challenge user
RUN useradd -m -s /bin/bash guest && echo 'guest:guest@222' | chpasswd

RUN cat >> /home/guest/.bashrc <<'EOF'
cat /etc/motd

# Reset challenge state on each login
cat > /tmp/backup_task.sh <<'EOF2'
#!/bin/bash
echo "Backup completed"
EOF2

EOF

RUN chown guest:guest /home/guest/.bashrc

# Create user flag
RUN echo 'FST{fake_flag_hahahaha}' > /home/guest/flag.txt \
    && chown guest:guest /home/guest/flag.txt \
    && chmod 644 /home/guest/flag.txt

# Create root flag
ARG ROOT_FLAG="FST{default_root_flag}"

RUN echo "ICODE{root_flag_751938413}" > /root/root_flag.txt \
    && chmod 600 /root/root_flag.txt

# Create vulnerable backup script
RUN cat > /home/guest/backup.sh <<'EOF2'
#!/bin/bash
# Simple backup script for the challenge
# TODO: ask admin to secure /tmp/backup_task.sh permissions
bash /tmp/backup_task.sh
EOF2

RUN chown root:root /home/guest/backup.sh \
    && chmod 755 /home/guest/backup.sh

# Create writable script executed by root through sudo backup.sh
RUN echo 'echo "Backup completed"' > /tmp/backup_task.sh \
    && chmod 777 /tmp/backup_task.sh

# Allow guest to run backup.sh as root without password
RUN echo 'guest ALL=(root) NOPASSWD: /home/guest/backup.sh' > /etc/sudoers.d/guest \
    && chmod 440 /etc/sudoers.d/guest

# SSH configuration
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config \
    && sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
