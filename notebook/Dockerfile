FROM python:3.11

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app/exercises

EXPOSE 8888

# Start the jupyter notebook server.
#   Runs without passwords or tokens. To make this secure in docker-compose
#   we bind to 127.0.0.1 instead.
# notebook < 7 shows an update banner. We need notebook < 7 because of
#   the `%autosave 30` magic command being currently broken for > 7.
CMD jupyter notebook --ip 0.0.0.0 --allow-root --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.show_banner=False
