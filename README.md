# Anti-Phishing API

API em Python e FastAPI para um projeto de análise de URLs suspeitas.

## Estado atual

A aplicação implementa `GET /health`, que retorna `{"message":"servidor funcionando!"}`.
Análise heurística, pontuação de risco e integração com inteligência de ameaças são objetivos futuros; ainda não estão implementados.

## Executar localmente

Na raiz do repositório:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app:app --app-dir src --reload
```

No Windows, ative com `.venv\Scripts\activate`.
A documentação interativa fica em http://localhost:8000/docs.

## Organização

| Caminho | Responsabilidade |
| --- | --- |
| `src/app.py` | Aplicação FastAPI e health check |
| `src/controllers/` | Espaço reservado para controladores |
| `src/services/` | Espaço reservado para regras de análise |
| `src/integrations/` | Espaço reservado para serviços externos |
| `src/config/` e `src/utils/` | Configuração e utilitários futuros |
| `tests/` | Estrutura inicial; ainda sem casos de teste |
| `requirements.txt` | Dependências do projeto |

## Próximos passos

- Implementar validação de URLs e análise heurística.
- Definir o contrato da resposta e os critérios de pontuação.
- Adicionar testes para as regras de análise.
- Integrar uma fonte externa de reputação.

Licença MIT; consulte [LICENSE](LICENSE).
