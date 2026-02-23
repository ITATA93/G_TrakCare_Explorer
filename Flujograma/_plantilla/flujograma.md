# Flujograma: [Nombre del Proceso]

## Diagrama Principal

```mermaid
flowchart TD
    Start([Inicio]) --> Step1[Paso 1]
    Step1 --> Decision1{¿Condición?}
    Decision1 -->|Sí| Step2[Paso 2A]
    Decision1 -->|No| Step3[Paso 2B]
    Step2 --> End([Fin])
    Step3 --> End

    %% Estilos
    classDef startEnd fill:#e1f5ff,stroke:#0066cc,stroke-width:2px
    classDef process fill:#fff4e1,stroke:#ff9900,stroke-width:2px
    classDef decision fill:#ffe1e1,stroke:#cc0000,stroke-width:2px

    class Start,End startEnd
    class Step1,Step2,Step3 process
    class Decision1 decision
```

## Leyenda

### Formas
- **Óvalo**: Inicio/Fin del proceso
- **Rectángulo**: Acción o proceso
- **Rombo**: Punto de decisión

### Colores
- 🔵 **Azul**: Inicio/Fin
- 🟡 **Amarillo**: Procesos/Acciones
- 🔴 **Rojo**: Decisiones

### Actores
- **[Actor 1]**: Responsable de [pasos específicos]
- **[Actor 2]**: Responsable de [pasos específicos]

## Notas del Diagrama

[Explicaciones adicionales sobre el flujo, casos especiales, o aclaraciones visuales]

---

**Última actualización**: [Fecha]
