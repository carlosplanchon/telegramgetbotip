FROM python
COPY . .
RUN python3.8 -m pip install requests
RUN python3.8 -m pip install --user -U telegramgetbotip
ENTRYPOINT python3.8 /root/.local/bin/telegramgetbotip -t token -i ids -v