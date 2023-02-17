FROM python:3.9
COPY . .
RUN pip install discord.py
RUN pip install python-dotenv
CMD ["python", "bot.py"]

