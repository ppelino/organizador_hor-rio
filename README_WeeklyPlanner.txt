# Planejador Semanal

O **Planejador Semanal** é uma aplicação interativa desenvolvida em Python para ajudar na organização de atividades semanais. Ele oferece uma interface gráfica para adicionar e alocar atividades, permitindo também exportar o planejamento para um arquivo PDF.

---

## Funcionalidades

- **Adição de Atividades**: Insira atividades personalizadas para organizar sua semana.
- **Grade Horária Interativa**: Dias da semana de segunda a sábado, com horários disponíveis das 08:00 às 18:00 (até 12:00 aos sábados).
- **Atribuição de Horários**: Clique diretamente na grade para alocar atividades nos dias e horários desejados.
- **Exportação para PDF**: Gere um planejamento semanal completo em formato PDF.

---

## Como Usar

### 1. Instalação

Certifique-se de que você tenha o Python 3.x instalado no seu sistema. Instale as dependências necessárias usando o comando abaixo:

```bash
pip install fpdf
```

### 2. Executar o Programa

Execute o script `schedule_professionals.py` com o comando:

```bash
python schedule_professionals.py
```

### 3. Adicionar Atividades

1. Insira o nome da atividade no campo "Atividade".
2. Clique no botão "Adicionar Atividade".

### 4. Atribuir Atividades

1. Clique em um botão na grade de horários para selecionar o dia e horário desejado.
2. A última atividade adicionada será alocada ao horário selecionado.

### 5. Exportar para PDF

1. Após organizar a grade horária, clique no botão "Exportar Planejamento para PDF".
2. O arquivo será salvo no caminho: `C:/Users/ppeli/OneDrive/Área de Trabalho/Horario/planejamento_semanal.pdf`.

---

## Estrutura do Código

### Classes Principais

- **WeeklyPlannerApp**: Contém toda a lógica para manipulação da interface gráfica, gerenciamento das atividades e exportação para PDF.

### Componentes

- **Grade Interativa**: Representada por botões dinâmicos que podem ser clicados para alocar atividades.
- **PDF Exporter**: Usa a biblioteca `FPDF` para gerar um arquivo PDF com a grade horária.

---

## Dependências

- `tkinter`: Para a interface gráfica.
- `fpdf`: Para geração de arquivos PDF.

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.

---

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
