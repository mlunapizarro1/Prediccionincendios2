# Fire Risk Prediction API

Esta API predice el nivel de riesgo de incendio forestal en una ubicación específica usando variables climáticas y de vegetación.

## Cómo usar

1. Entrena el modelo:
```bash
python train_model.py
```

2. Inicia la API:
```bash
uvicorn app.main:app --reload
```

3. Accede a la documentación automática en:
```
http://127.0.0.1:8000/docs
```
