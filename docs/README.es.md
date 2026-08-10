<p align="center">
  <img src="../assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <a href="../README.md">English</a> ·
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.zh-TW.md">繁體中文</a> ·
  <a href="./README.ja.md">日本語</a> ·
  <a href="./README.ko.md">한국어</a> ·
  <strong>Español</strong>
</p>

<p align="center">
  <strong>v3.0.0</strong> · MIT · 6 locales · prosa / copy / microcopy de GUI
</p>

<p align="center">
  <a href="#instalación">Instalación</a> ·
  <a href="#cómo-funciona">Cómo funciona</a> ·
  <a href="#antes-y-después">Antes y después</a> ·
  <a href="#de-dónde-salen-las-reglas">Fuentes</a> ·
  <a href="#perfiles-de-locale">Perfiles de locale</a> ·
  <a href="#estructura-del-repositorio">Estructura del repositorio</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">Incidencias</a>
</p>

<p align="center"><strong>Decide qué contenido debe aparecer en el producto y redáctalo con naturalidad en seis locales.</strong></p>

Humanization reúne métodos prácticos de proyectos consolidados de escritura, edición, localización, diseño de contenidos y anti-slop. Está pensado para quienes crean productos multilingües y trabajan con prosa, relatos, documentación, contenido de producto, textos de marketing, correo electrónico, publicaciones sociales y textos de GUI como navegación, botones, errores, estados vacíos, confirmaciones, notificaciones, avisos de privacidad y nombres accesibles. Antes de reescribir, distingue los datos internos sobre capacidades de los mensajes que los usuarios necesitan realmente en la superficie seleccionada.

**Perfiles de locale:** [zh-CN 简体中文](../humanization/references/locales/zh-CN.md) · [zh-TW 繁體中文](../humanization/references/locales/zh-TW.md) · [en English](../humanization/references/locales/en.md) · [ja 日本語](../humanization/references/locales/ja.md) · [ko 한국어](../humanization/references/locales/ko.md) · [es Español](../humanization/references/locales/es.md)

## Cómo funciona

Cada tarea combina tres módulos con responsabilidades bien delimitadas.

- **Contrato común:** hechos, fuentes, capacidades, privacidad, CTA, términos de marca, placeholders, edición mínima, calibración de la voz a partir de una muestra del autor (solo para la tarea en curso) y el filtro que decide si cada contenido debe existir en esa superficie.
- **Perfil de locale:** sintaxis, registro u honoríficos, puntuación, vocabulario regional, rastros de traducción literal y ritmo natural.
- **Microcopy de GUI:** redacción específica para botones, errores, estados vacíos, confirmaciones y notificaciones, con protección de claves, mensajes ICU, variables, markup y estructura en tiempo de ejecución.

El contrato común clasifica primero cada candidato como `keep`, `rewrite`, `move` o `remove`. Si el candidato también deja al descubierto una acción, un estado o una ruta de recuperación que falta, añade `needs_product_decision` al flujo subyacente. Los datos internos delimitan lo que el producto puede afirmar, pero no pasan automáticamente a la interfaz. Después, los perfiles de locale expresan con naturalidad los mensajes aprobados. Las traducciones pueden cambiar de estructura y longitud, pero conservan el público, la acción, el alcance real de las capacidades, las promesas de privacidad y la terminología aprobada.

Si el material de partida está incompleto, la Skill formula una pregunta concreta, comprueba una fuente o reduce el alcance de la afirmación. Si una página carece de una acción o ruta de recuperación respaldada por el producto, devuelve `needs_product_decision`; una explicación no sustituye ese flujo pendiente. Las comprobaciones deterministas dan error ante daños demostrables. La pertinencia del mensaje, el tono y la naturalidad se revisan según el contexto.

## Antes y después

Humanization no convierte en texto publicable cada frase que sea cierta. Primero comprueba qué función cumple en esa superficie y después decide si debe reescribirse, trasladarse o desaparecer del contenido público.

| Antes | Después |
| :--- | :--- |
| **Inventario interno de capacidades**<br><br>«Esta página no tiene servicio de procesamiento, no acepta archivos, no se conecta a sistemas externos y no ofrece una acción para iniciar una tarea». | **No se añade ningún texto público en su lugar.**<br><br>**Destino del texto:** `remove`<br>**Flujo de producto:** `needs_product_decision`. ¿Esta página es solo informativa o debería permitir completar una tarea? Si la tarea corresponde a esta página, primero hay que implementar un punto de entrada y una CTA reales. |
| **Hechos ocultos entre frases grandilocuentes**<br><br>«Como parte de nuestro compromiso continuo con la mejora de la experiencia de usuario, realizamos un análisis exhaustivo de 42 solicitudes de soporte y descubrimos un dato importante que merece atención: en 31 se mencionaban dificultades para vincular una cuenta». | **Revisamos 42 solicitudes de soporte. En 31 se mencionaban problemas al vincular una cuenta.**<br><br>**Destino del texto:** `rewrite` |
| **Hechos unidos con un contraste innecesario**<br><br>«La nueva vista no solo reúne las facturas pendientes, sino que también las ordena por fecha de vencimiento». | **La nueva vista reúne las facturas pendientes y las ordena por fecha de vencimiento.**<br><br>**Destino del texto:** `rewrite` |
| **Error que permite volver a intentarlo**<br><br>«Error 500: la solicitud de guardado falló porque el worker agotó el tiempo de espera». | **No se pudieron guardar los cambios. Inténtalo de nuevo.**<br><br>**Mensaje público:** `rewrite`<br>**Diagnóstico de desarrollo:** `move` a los registros |
| **Estado vacío con una acción disponible**<br><br>«No hay datos». | **Ningún resultado coincide con estos filtros. Al borrar los filtros se mostrarán todos los elementos.**<br><br>**Destino del texto:** `rewrite` |

Ningún ejemplo inventa funciones ni vías de recuperación. El texto sin una función para el usuario se elimina, los datos `42/31` se conservan, los contrastes vacíos se sustituyen por afirmaciones directas, los diagnósticos se trasladan a la superficie adecuada y el estado vacío solo remite a una acción disponible.

## De dónde salen las reglas

Humanization se apoya en métodos y guías que otros proyectos han compartido públicamente. Agradecemos a los siguientes proyectos sus aportaciones al contrato común, los perfiles de locale y el flujo de edición.

| Proyecto | Contribución a Humanization |
| :--- | :--- |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) | Aportó la base inicial para textos extensos en `zh-CN`: suficiencia del material, comprobación de fuentes, límites entre realidad y ficción, flujo de revisión y ritmo natural del chino. |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop/tree/96d1ca568a1db7e1ef9a381644c744440f816ee4) | Ayudó a definir una revisión textual que prefiere la información concreta a los eslóganes, elimina la decoración antes de reescribir y usa las coincidencias con patrones como indicios para revisar. |
| [ehmo/slopkit (`slopbeth`)](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | Inspiró el inventario de evidencias para entidades, números, fechas, URL, citas e incertidumbre, de modo que cada afirmación permanezca dentro de lo que permiten las pruebas disponibles. |
| [blader/humanizer](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md) | Inspiró el ajuste de la voz para una sola tarea a partir de una muestra elegida expresamente por el usuario: se observan los ritmos recurrentes, los comienzos de párrafo, el vocabulario, el registro, los pronombres, la puntuación, las repeticiones, las transiciones, la forma de expresar la incertidumbre y los rasgos deliberados, sin crear un perfil permanente del autor. |
| [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) | Inspiró el flujo de edición mínima: conservar los hechos y la voz que ya funciona, hacer el cambio útil más pequeño y permitir `no_change`. |
| [18F/content-guide](https://github.com/18F/content-guide/tree/1b1723d3d5b8f91d92c16487c88b56265dc0ec3a) y [GOV.UK Design System](https://github.com/alphagov/govuk-design-system/tree/efb0d77d38b7ed7f921697564d2c47723d434977) | Ayudaron a definir el filtro basado en las necesidades del usuario, las instrucciones orientadas a tareas, la colocación de los mensajes y el requisito de ofrecer un siguiente paso real en errores y estados de indisponibilidad. |
| [Shopify Polaris](https://github.com/Shopify/polaris-react-archive/blob/af6ffb66a5b1d20f6c2c898b334a1ebb53728ba2/polaris.shopify.com/content/content/fundamentals.mdx), [Carbon Design System](https://github.com/carbon-design-system/carbon-website/tree/e14433309b1dd53ec790eaa176139007ea9e9c80) y [PatternFly](https://github.com/patternfly/patternfly-org/tree/3aff87cace31c7d7e94ebae4cb35666f4f2e75d7) | Guiaron la selección de contenido por componente: conservar la ayuda pertinente para la tarea, distinguir los estados de la interfaz y vincular las limitaciones con consecuencias observables y acciones que el producto admite. |
| [ya8282/ux-writing-skill](https://github.com/ya8282/ux-writing-skill/tree/711e4162d21367bc62003e428696dc76807d56ec), [OOOOuyang/UX-writing-skill](https://github.com/OOOOuyang/UX-writing-skill/tree/fad02668533dca76d638aaacf6c2e834657df0ab) y [RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) | Ayudaron a definir decisiones explícitas sobre el destino de cada contenido, el principio de que cada texto auxiliar debe justificar su presencia y la separación entre los mensajes de recuperación para usuarios y los diagnósticos para desarrollo. |

## Perfiles de locale

Cada perfil reúne la sintaxis, el registro, la puntuación, la terminología, la revisión de calcos y el ritmo propios de su locale.

| Locale | Proyectos y guías de referencia | Principios derivados de estas fuentes |
| :--- | :--- | :--- |
| `zh-CN` | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) y [GB/T 15834-2011](https://openstd.samr.gov.cn/) | Sintaxis y terminología de China continental, puntuación de ancho completo, escritura extensa guiada por el material y un estilo editorial propio para `zh-CN prose`. |
| `zh-TW` | [Guía de estilo zh-TW de Mozilla](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md) y [bruce6731/anti-ai-writing-taiwan](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | Localización nativa de `zh-TW`, con terminología, registro, puntuación y orden cultural propios de Taiwán. |
| `en` | [Google styleguide](https://github.com/google/styleguide/tree/gh-pages/docguide), [Microsoft Writing Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide) y [Digital.gov Plain Language](https://digital.gov/guides/plain-language/) | Relaciones claras entre actor y acción, documentación concisa, voz de marca adaptada al contexto, coherencia regional y uso natural de la puntuación inglesa. |
| `ja` | [Guía de estilo japonés de Mozilla](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md), [chezou/slop-nuki](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7), [iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2), [RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) y [coji/natural-japanese](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | Elipsis y orden natural de las palabras, partículas, honoríficos y atenuación según el contexto, formas nominales y verbales adaptadas al componente, integridad de recursos de GUI y revisión calibrada por densidad y género. |
| `ko` | [Guía de estilo coreano de Mozilla](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md), [dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad) y [HarryJhin/korean-writing](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | Elipsis natural del sujeto, partículas y espaciado, niveles de habla `합니다`/`해요`/`다`, conservación de honoríficos, terminaciones y revisión de calcos del inglés y el japonés. |
| `es` | [Guías de estilo en español de Mozilla](https://github.com/mozilla-l10n/styleguides/tree/main/docs/es) | Concordancia, clíticos, tratamiento con `tú`/`usted`/`ustedes`, mayúscula inicial en la interfaz, terminología regional, puntuación y revisión de calcos del inglés. |

Los proyectos enlazados conservan sus propias licencias. [Las notas de investigación multilingüe](../research/multilingual-skill-research.md), [el informe sobre qué copy de GUI debe existir](../research/gui-copy-existence-gate.md) y [el estudio de `blader/humanizer`](../research/blader-humanizer.md) documentan las fuentes y la aportación de cada una a Humanization; consulta la licencia de cada repositorio enlazado antes de reutilizar su texto o código. Las instrucciones específicas de Humanization se redactaron a partir de las prácticas resumidas arriba.

## Instalación

Pide a un agente compatible con la instalación de Skills desde GitHub que haga lo siguiente:

```text
Instala la Skill humanization desde https://github.com/thevenomsnake/humanization. La Skill se encuentra en el directorio humanization/.
```

El directorio instalado debe conservar el nombre `humanization`. La tarjeta correcta se llama `Humanization`, usa un icono H verde oscuro con seis barras de idioma e incluye el texto “Natural writing and GUI copy across six locales.” Si Codex muestra `活人感写作`, está enseñando la Skill antigua `human-writing`.

<details>
<summary><strong>Instalación manual</strong></summary>

Copia el directorio [`humanization`](../humanization) del repositorio en tu directorio de Skills de Codex:

```text
$CODEX_HOME/skills/humanization/
```

</details>

Úsala indicando de forma explícita el locale, el formato y la superficie:

```text
Usa $humanization con locale=ja, format=web-microcopy y surface=error. Reescribe estos mensajes de error sin alterar la CTA, los términos de marca, los placeholders ni la estructura del recurso de origen.
```

Antes de reescribir, revisa si el contenido actual debe permanecer en la superficie donde aparece:

```text
Usa $humanization con locale=zh-CN, format=web-microcopy y surface=public-page. Clasifica cada afirmación sobre capacidades como keep, rewrite, move o remove, y señala cualquier decisión de producto subyacente.
```

El nombre público de formato `web-microcopy` cubre textos de GUI en HTML, JSON, YAML, ARB, PO, código fuente y archivos de diseño para productos web, de escritorio y móviles.

Ejecuta el validador determinista con las mismas opciones explícitas:

```bash
python humanization/scripts/check_writing.py --locale en --format copy draft.md
python humanization/scripts/check_writing.py --locale es --format web-microcopy --source source.json target.json
```

## Qué cambió en 3.0.0

- Se consolidó `humanization` como nombre estable de la Skill y del directorio, con `Humanization` como nombre visible en la interfaz.
- Las instrucciones de ejecución se organizaron en un contrato común, seis perfiles de locale y un módulo de microcopy de GUI.
- Se incorporaron principios de información concreta, contención y revisión mediante indicios a partir de `kill-ai-slop`.
- Se añadió un filtro multilingüe que separa los datos internos sobre capacidades de los mensajes que deben publicarse para los usuarios.
- `--locale` y `--format` pasaron a ser explícitos; los textos mixtos se enrutan de forma deliberada y las valoraciones de tono se presentan como avisos para revisión.

Consulta [CHANGELOG.md](../CHANGELOG.md) para ver el historial completo.

## Estructura del repositorio

<details>
<summary><strong>Mostrar el directorio completo</strong></summary>

```text
humanization/
├── SKILL.md
├── VERSION
├── LICENSE
├── agents/
│   └── openai.yaml
├── assets/
│   ├── icon-small.png
│   └── icon-large.svg
├── references/
│   ├── core.md
│   ├── locales/
│   │   ├── zh-CN.md
│   │   ├── zh-TW.md
│   │   ├── en.md
│   │   ├── ja.md
│   │   ├── ko.md
│   │   └── es.md
│   ├── formats/
│   │   ├── expressive-text.md
│   │   └── gui-microcopy.md
│   ├── forum-prose.md
│   ├── reality.md
│   ├── fiction.md
│   ├── formats.md
│   └── revision.md
└── scripts/
    ├── check_common.py
    ├── check_gui.py
    ├── check_locale.py
    ├── check_writing.py
    ├── check_writing_smoke.py
    ├── check_zh_cn.py
    └── check_prose.py
```

| Ruta | Función |
| :--- | :--- |
| [`SKILL.md`](../humanization/SKILL.md) | Dirige cada tarea a los módulos común, de locale y de formato. |
| [`core.md`](../humanization/references/core.md) | Reúne hechos, fuentes, capacidades, privacidad, CTA, términos de marca, placeholders, edición mínima y la decisión de conservar, reescribir, mover o retirar cada contenido. |
| [`locales/`](../humanization/references/locales) | Contiene los seis perfiles de escritura nativa. |
| [`expressive-text.md`](../humanization/references/formats/expressive-text.md) | Cubre textos no vinculados a una GUI: producto, documentación, marketing, correo electrónico y publicaciones sociales. |
| [`gui-microcopy.md`](../humanization/references/formats/gui-microcopy.md) | Define el filtro de contenido para GUI, la función de cada componente y la protección de recursos estructurados. |
| [`check_writing.py`](../humanization/scripts/check_writing.py) | Ofrece una única CLI para las comprobaciones comunes, de locale y de GUI. |
| [`check_zh_cn.py`](../humanization/scripts/check_zh_cn.py) | Mantiene el comprobador original de acciones limitado a `zh-CN prose`. |

</details>

## Atribución y comentarios

Humanization se distribuye bajo la licencia MIT. Su base inicial para textos extensos en `zh-CN` procede de [KKKKhazix/human-writing v1.1.0](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192), también publicado bajo la licencia MIT. El mapa de fuentes anterior reconoce los proyectos y las guías que dieron forma a la arquitectura actual y explica la aportación de cada uno.

Para informar de conflictos entre reglas, falsos positivos o fallos específicos de un modelo, [abre una incidencia](https://github.com/thevenomsnake/humanization/issues) e incluye el prompt, la salida relevante y el resultado que esperabas.

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
