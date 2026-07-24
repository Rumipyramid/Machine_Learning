# Back to Basics — Fuerza de Venta Vida Individual

*Behavioral Design · RIMAC · Q3 2026*

---

## Contexto

**El problema de negocio.** La Fuerza de Venta de Vida Individual necesita fortalecer tres cosas
a la vez: cómo agenda citas, cómo forma a sus asesores (especialmente a los nuevos) y cómo genera
leads de forma sostenible. Hoy el asesor navega con herramientas dispersas, sin una estrategia de
contacto unificada y sin un modelo de venta consultiva estandarizado — cada quien vende "a su
manera", con curvas de aprendizaje largas para los asesores junior.

**El riesgo legal que lo hace urgente.** Más de la mitad de la venta de Vida Individual nace de
contacto que hoy no tiene opt-in previo. La Ley 32323 (vigente 2025, "ley antispam") prohíbe la
comunicación comercial sin consentimiento previo, expreso e inequívoco, y la fiscalización ya es
activa en el sistema financiero: sanciones de hasta 450 UIT (~S/2.4M), con casos ya aplicados
(BBVA por una sola llamada, Scotiabank por más de S/2.4M). El componente CUA (gestión del
consentimiento) se integró dentro de Back to Basics como parte del mismo problema, no como
iniciativa aparte: no se puede rediseñar la estrategia de contacto sin resolver primero cómo se
contacta de forma legal.

**El problema conductual detrás.** Dos mecanismos explican por qué el asesor no rinde lo que
podría: (1) sobrecarga cognitiva — demasiadas herramientas y materiales sin estructura, lo que
degrada la toma de decisión incluso de un vendedor experimentado; (2) ausencia de un modelo de
formación con práctica espaciada y feedback — el onboarding actual no sostiene el aprendizaje en
el tiempo, así que el ramp-up de un asesor junior es lento y costoso.

**Por qué importa a nivel de negocio.** Perú tiene una penetración de seguros de ~2.08% del PBI
(vs. 4.6% en Chile), una tenencia de solo ~4 de cada 10 personas, y ~48% de la población desconfía
del seguro — la causa #1 declarada es la falta de información. El asesor es, en la práctica, el
punto de contacto humano que puede revertir esa desconfianza si tiene la estrategia y las
herramientas correctas para hacerlo.

**Prioridad.** El comité de CoE X ya elevó Back to Basics a **prioridad #1** del trimestre.
Equipo: Melissa y Alejandro, junto con César (Lead de Service Design, de otro equipo).

---

## Entregables V1

La primera tanda del proyecto cubre **toda la creación de contenido y herramientas** del modelo de
venta. Organizados por lo que resuelven, no por el orden en que se hicieron:

### Evidencia que sostiene el diseño
- **Desk research y bench de estrategias de contacto** en frío vs. caliente: qué gatillos abren
  una conversación (reciprocidad, curiosidad, personalización).
- **Sacrificial concepts**: seis conceptos de contacto probados con no-clientes para elicitar
  objeciones reales antes de invertir en el diseño final, específicamente para el escenario sin
  CUA.
- **Validación con stakeholders** en cada hito, para que el diseño no avance sin alineamiento.

### Estrategia de contacto (el corazón legal y conductual del proyecto)
- **Informe de estrategia de primer contacto** validado en conjunto con Legal, Cumplimiento y
  CUA: qué canal, qué momento y qué mensaje maximizan la respuesta sin fricción normativa —
  cubriendo tanto el escenario con CUA como el escenario sin CUA.
- **Plantillas de WhatsApp y correo** de primer contacto, con personalización y mínima fricción de
  respuesta, para el flujo con consentimiento (la versión para el flujo sin consentimiento está en
  construcción).

### Playbook y materiales de venta
- **Modelo de venta consultiva**: arquitectura de la conversación basada en preguntas de
  descubrimiento que anclan la oferta en las motivaciones del cliente, no en el producto.
- **Playbook de storytelling de asesoría**: encuadre narrativo — historias que activan
  identificación y emoción donde la cifra sola no persuade.
- **Materiales de venta** (flyer, brochure, cartaplan) simplificados para reducir la carga
  cognitiva del mensaje y jerarquizar visualmente los beneficios.
- **Materiales actualizados con statement de vida + motivaciones**: pitch segmentado por perfil
  motivacional del cliente, con el statement de vida como compromiso público del asesor.

### Formación del asesor
- **Universidad Vida — Onboarding**: formación de hábitos tempranos con práctica espaciada y
  feedback inmediato desde el día 1.
- **Universidad Vida — Modelo de competencias**: progresión por niveles con evaluación y
  reconocimiento, para sostener la motivación del asesor en el tiempo (no solo al inicio).
- **AIDA Skill Trainer** (co-diseño): simulador de práctica deliberada — role-play con IA y
  feedback inmediato que acelera la curva de aprendizaje sin costo de clientes reales.

### Validación antes de escalar
Cuatro hitos de piloto en curso para calibrar el modelo con datos reales de campo antes del
despliegue completo: una calibración inicial, una prueba en campo, una segunda calibración con
esa evidencia, y una validación técnica de que el copiloto de IA reproduce fielmente el modelo
calibrado.

### Despliegue
Estrategia de adopción diseñada para dos frentes — la fuerza de venta actual (defaults,
recordatorios, campeones internos) y Universidad Vida (adopción por cohortes con hitos visibles y
reconocimiento) — para que las nuevas prácticas se sostengan más allá del lanzamiento.

**Impacto esperado de la V1:** ↓ curva de aprendizaje y +conversión de venta; −25–40% en tiempo de
ramp-up de asesores junior (estimado); +20–30% en agendamiento de citas (estimado); ahorro
proyectado de S/1.8M vía AIDA.

---

## Siguientes pasos

### 1. Evolución del entrenamiento

Pasar de un onboarding puntual a un **programa de crecimiento continuo**: modelo por competencias
+ calendarización con práctica espaciada + programa de crecimiento del asesor más allá del primer
mes. La práctica espaciada supera consistentemente a la práctica masiva en retención de
aprendizaje — este paso extiende esa misma lógica del onboarding al desarrollo de mediano plazo.

En paralelo, evolucionar **AIDA de piloto a herramienta funcional** de uso diario para el asesor
(no solo para el comité) — para esto se necesita una reunión con el equipo de GenAI que defina
alcances conjuntos.

### 2. Adaptación del proyecto a otros canales de venta Vida

Antes de saltar a otro ramo, escalar el playbook y la estrategia de contacto **dentro de Vida**:
a los demás canales de venta (no solo el canal donde se construyó la V1). Es la fase de
transversalización más segura porque el producto no cambia, solo el canal.

### 3. Adaptación a otro ramo: AMI

Una vez transversalizado dentro de Vida, llevar la **metodología** de Back to Basics —no solo
piezas de comunicación— al ramo AMI: estrategia de contacto, playbook de venta y arquitectura de
decisión adaptados a las particularidades de ese producto.

Esto es distinto del proyecto de guías resumidas de AMI Relanzamiento (que resuelve entendimiento
de producto, no modelo de venta) — aquí se trata de escalar el *modelo de venta* que Back to
Basics ya validó en Vida, no las piezas de comunicación de un producto específico.

### 4. Estrategias para mitigar el golpe de CUA

Dos frentes concretos, pensados para trabajar en conjunto:

**Alertas de CRM.** Arquitectura de fricción deliberada: avisar al asesor si el cliente pidió no
ser contactado, o condicionar directamente el contacto a tener el consentimiento registrado —
un default seguro dentro del CRM que protege a RIMAC del riesgo legal sin depender de que el
asesor recuerde revisarlo. Requiere coordinación con el equipo dueño del CRM.

**Programa de referidos.** En vez de contactar en frío, activar el contacto por **referido de un
cliente existente**: la introducción cálida trae consigo un consentimiento implícito y evita por
completo el riesgo de contacto no autorizado — no es solo una mitigación legal, también convierte
mejor que el contacto en frío por dos mecanismos conductuales conocidos: prueba social (el cliente
existente ya validó el producto) y reciprocidad (referir es un favor que el asesor puede
reconocer). Queda por definir la mecánica de incentivo para el cliente que refiere.

---

## Resumen para la conversación con Milagros

| | |
|---|---|
| **Qué ya está construido** | Estrategia de contacto, playbook de venta, materiales, Universidad Vida y AIDA — validados con evidencia propia y con Legal/Cumplimiento/CUA |
| **Qué falta para cerrar la V1** | Cuatro pilotos de calibración del modelo antes del despliegue completo |
| **Qué viene después** | Entrenamiento continuo, más canales de Vida, el ramo AMI, y dos mitigaciones concretas al riesgo de CUA |
| **Por qué ahora** | Prioridad #1 del comité; más del 50% de la venta actual depende de resolver el problema de contacto sin consentimiento |
