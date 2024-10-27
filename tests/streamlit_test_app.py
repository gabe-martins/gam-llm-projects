import streamlit as st 
from datetime import datetime, timedelta

def get_datetime(date_arg='hour', time=1):
  today = datetime.now()
  if date_arg.lower() == 'hour':
    min_datetime = today - timedelta(hours=time)
    max_datetime = today + timedelta(hours=1)
    return min_datetime.strftime("%Y-%m-%dT%H:00:00.000Z"), max_datetime.strftime("%Y-%m-%dT%H:00:00.000Z")
    
  elif date_arg.lower() == 'day':
    min_datetime = today - timedelta(days=time)
    max_datetime = today + timedelta(days=1)
    return min_datetime.strftime("%Y-%m-%dT00:00:00.000Z"), max_datetime.strftime("%Y-%m-%dT00:00:00.000Z")

# Defina a lista de opções
time_options =[
  {
    "option": "1 hora",
    "date_arg": "hour",
    "time": 1
  },
  {
    "option": "2 horas",
    "date_arg": "hour",
    "time": 2
  },
  {
    "option": "6 horas",
    "date_arg": "hour",
    "time": 6
  },
  {
    "option": "12 horas",
    "date_arg": "hour",
    "time": 12
  },
  {
    "option": "24 horas",
    "date_arg": "hour",
    "time": 24
  },
  {
    "option": "2 dias",
    "date_arg": "day",
    "time": 2
  },
  {
    "option": "3 dias",
    "date_arg": "day",
    "time": 3
  },
  {
    "option": "5 dias",
    "date_arg": "day",
    "time": 5
  },
  {
    "option": "7 dias",
    "date_arg": "day",
    "time": 7
  },
  {
    "option": "10 dias",
    "date_arg": "day",
    "time": 10
  },
  {
    "option": "15 dias",
    "date_arg": "day",
    "time": 15
  },
  {
    "option": "30 dias",
    "date_arg": "day",
    "time": 30
  }
]
options = [opc['option'] for opc in time_options]
selecao = st.selectbox('Selecione uma opção de tempo:', options)

st.write(f'Você selecionou: {selecao}')

if selecao:
  for opc in time_options:
    if opc['option'] == selecao:
      min_datetime, max_datetime = get_datetime(date_arg=opc['date_arg'], time=opc['time'])
      st.write(f'''{min_datetime} | {max_datetime}''')