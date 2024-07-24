FROM archlinux:latest

WORKDIR /app

RUN pacman -Syu --noconfirm && \
    pacman -S python python-pip --noconfirm 

COPY requirements.txt .

RUN python -m pip install -r requirements.txt --break-system-packages

COPY ./src/ .

ENV PORT=8080 \
    HOST="0.0.0.0"

EXPOSE 8080

CMD [ "python", "app.py" ]