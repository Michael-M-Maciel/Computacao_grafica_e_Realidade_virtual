# 🛡️ Cerco Escolar UNIFG | Motor de Inteligência Artificial (Back-End)

Este repositório contém a infraestrutura em Python que compõe o núcleo do sistema **Cerco Escolar**. Ele expõe rotas HTTP via **Flask**, gerencia dados locais e atua de maneira assíncrona recebendo streams de câmeras e aplicando algoritmos state-of-the-art de Visão Computacional.

## 🧠 Arquitetura de IA Aplicada

O sistema executa modelos locais via biblioteca `ultralytics` para não depender de nuvem, priorizando a latência.

* **Modelo de OCR & LPR (Câmera 01 - Placas):**
    Utiliza um modelo customizado `best.pt` para extração de RoI (Region of Interest) focado em placas do Mercosul/Brasil. Após o corte via OpenCV, a imagem é enviada a um módulo próprio (`src.leitor_ocr`) para a transcrição. Para evitar "ruídos" óticos, implementamos uma lógica de *Urna de Votação*, exigindo redundância de leituras antes do alerta ser emitido.
* **Modelo de Análise de Comportamento (Câmera 02 - Pátio):**
    Aplica o `yolov8n-pose.pt` acoplado a um tracker (`bytetrack.yaml`) para extrair nós esqueléticos (Keypoints). A lógica matemática central foca em calcular instâncias vetoriais dinâmicas para medir a colisão entre eixos periféricos (Mãos e Pés) e troncos em velocidades específicas, traduzindo impacto em uma classificação de "Briga/Conflito Físico".

## 🚀 Estrutura de Diretórios Automáticos

Para que o back-end opere isolado de bancos remotos complexos, ao inicializar (`app.py`), o servidor confere a integridade do espaço alocado:

* `capturas_placas/`: Exporta frames (evidências em `.jpg`) toda vez que um carro restrito ou desconhecido tenta quebrar a barreira.
* `ocorrencias_briga/`: Gera sub-pastas assíncronas documentando de 1 a 5 frames exatos do momento e epicentro do conflito físico.
* `fotos_funcionarios/`: Permite o Upload assíncrono via `multipart/form-data` e armazenagem segura de perfis de docentes via CRUD.
* Arquivos `*.json` (veiculos, usuarios, notificações): Simuladores de Banco de Dados local que mantêm os fluxos salvos.

## 🔌 API & Endpoints

O back-end opera em rotas altamente parametrizadas, divididas entre processamento e chamadas RESTful puras.

| Método | Endpoint | Função/Retorno |
| :--- | :--- | :--- |
| `POST` | `/api/login` | Retorna um status de autorização e injeta o Session Cookie. |
| `GET` | `/video_feed/<modulo>` | Realiza o *Video Streaming* `multipart/x-mixed-replace`. |
| `GET` | `/api/alertas` | Consumido em Polling contínuo pelo Frontend. Retorna o array transiente com as notificações visuais. |
| `CRUD` | `/api/veiculos` | Cadastro de placas restritas e autorizadas (Role: Admin). |
| `CRUD` | `/api/funcionarios` | Associação de OCR com funcionário + `request.files.get('foto')`. |

## 🛠️ Instalação e Execução

Para testes em ambiente de desenvolvimento local:

1. Instale o Python (recomendado `^3.10`).
2. Crie um ambiente virtual: `python -m venv venv` (opcional, mas recomendado).
3. Instale os requisitos principais:
   ```bash
   pip install flask opencv-python ultralytics numpy