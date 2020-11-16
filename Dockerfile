FROM python:3
WORKDIR /usr/src/app

COPY ip_print_final.py  /usr/src/app
COPY input1.json /usr/src/app
COPY input2.json /usr/src/app

CMD [ "python", "./ip_print_final.py", "input1.json" ]
CMD [ "python", "./ip_print_final.py", "input2.json" ]