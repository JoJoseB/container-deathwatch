# Container Deathwatch

O **Container Deathwatch** é um script em python para monitorar containers Docker que entram no estado de **"die"** (morte). Ele permite a identificação rápida de containers que falharam, oferecendo informações detalhadas sobre os eventos que ocorreram antes da falha e ajudando a diagnosticar problemas em ambientes de containers.

## Funcionalidades

- Monitoramento em tempo real de containers Docker que entram em estado "die"
- Notificações automáticas enviadas para o **Discord** via **webhook** sempre que um container falha.

## Como Usar

1. Configurar a API do docker para escutar requisições na interface de rede 

  ```bash
  sudo nano /usr/lib/systemd/system/docker.service
  ```

2. Modificiar a seguinte linha

  ```bash
  #ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
  ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375 --containerd=/run/containerd/containerd.sock
  ```

3. Para as modificações entrarem em vigor reinicie o docker (Ubuntu)

  ```bash
  sudo systemctl daemon-reload
  sudo systemctl restart docker
  ```

4. Clonar o repositório e entrar no diretório do projeto

  ```bash
  git clone https://github.com/JoJoseB/container-deathwatch.git
  cd container-deathwatch
  ```

5. Criar um ambiente virual do python e instalar as dependencias com pip

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

6. Em um canal do discord crie uma url webhook crie um arquivo .env dentro do diretório do projeto e preecha o arquivo com informações aproximadamente assim

  ```bash
  DISCORD_WEBHOOK="https://discordapp.com/api/webhooks/1349134904855891978/zW9KNZ0HUyOUKK-ncWRj_yz8jHXCBk2btuBaSGURGtw7SRm4yS7qR7C-3GU4qu7IIKzR"
  ```
7. Agora execute o arquivo Python

  ```bash
  python3 deathwatch.py
  ```

8. Para verificiar se está funcionando rode o teste que as mensagens devem aparecer no canal do discord

  ```bash
  for i in `seq 5`; do docker run -d nginx; done; docker stop `docker ps -q`
  ```