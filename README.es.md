<p align="center">
  <img src="./assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <a href="./README.md">English</a> ·
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
  <a href="#de-dónde-salen-las-reglas">Fuentes</a> ·
  <a href="#perfiles-de-locale">Perfiles de locale</a> ·
  <a href="#estructura-del-repositorio">Estructura del repositorio</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">Incidencias</a>
</p>

<p align="center"><strong>Escribe y revisa textos en seis locales sin trasladar las reglas de un idioma a los demás.</strong></p>

Humanization es una Skill de Codex con mantenimiento independiente para prosa, relatos, documentación, contenido de producto, textos de marketing, correo electrónico y publicaciones sociales. También trabaja con textos de GUI como navegación, botones, errores, estados vacíos, confirmaciones, notificaciones, avisos de privacidad y nombres accesibles.

**Perfiles de locale:** [zh-CN 简体中文](./humanization/references/locales/zh-CN.md) · [zh-TW 繁體中文](./humanization/references/locales/zh-TW.md) · [en English](./humanization/references/locales/en.md) · [ja 日本語](./humanization/references/locales/ja.md) · [ko 한국어](./humanization/references/locales/ko.md) · [es Español](./humanization/references/locales/es.md)

## Cómo funciona

Cada tarea carga tres módulos, cada uno con una función acotada.

- **Contrato común:** hechos, fuentes, capacidades, privacidad, CTA, términos de marca, placeholders y edición mínima.
- **Perfil de locale:** sintaxis, registro u honoríficos, puntuación, vocabulario regional, calcos de traducción y ritmo natural.
- **Microcopy de GUI:** redacción específica para botones, errores, estados vacíos, confirmaciones y notificaciones, con protección de keys, mensajes ICU, variables, markup y estructura de ejecución.

El contrato común mantiene estables las afirmaciones de hecho y las promesas del producto en todos los idiomas. Los perfiles de locale deciden cómo expresar esas restricciones de forma natural en cada lugar. Las traducciones pueden usar estructuras y longitudes distintas, pero deben conservar el mismo público, acción, límite de capacidad, promesa de privacidad y terminología aprobada.

Cuando el material de origen está incompleto, la Skill formula una pregunta concreta, consulta una fuente o reduce el alcance de la afirmación. Cuando el original ya funciona, lo deja intacto. Las comprobaciones deterministas solo bloquean daños que pueden demostrar; el tono y la naturalidad siguen siendo decisiones de revisión del perfil de locale seleccionado.

## De dónde salen las reglas

Humanization adapta mecanismos de edición de otros proyectos y los reescribe para esta arquitectura. No copia su redacción, ejemplos, scripts ni listas de palabras.

| Proyecto | Qué adoptó Humanization | Qué quedó fuera |
| :--- | :--- | :--- |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) | La base de escritura extensa en `zh-CN`: suficiencia del material, comprobación de fuentes, límites entre realidad y ficción, flujo de revisión y ritmo natural del chino. | Las reglas editoriales de puntuación y frases de contraste en chino permanecen dentro de `zh-CN prose`; no son reglas globales. |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop) | Principios exclusivamente textuales: preferir información concreta a los eslóganes, quitar la decoración antes de reescribir y tratar las coincidencias con patrones como indicios para revisar, no como veredictos. | Colores, tipografía, tarjetas, esquinas, iconos, movimiento, estilo de botones y analizadores visuales. |
| [ehmo/slopkit (`slopbeth`)](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | El inventario sujeto a evidencia para entidades, números, fechas, URL, citas e incertidumbre; la evidencia ausente no se rellena con afirmaciones inventadas. | Prohibiciones de palabras en inglés, reglas sobre la raya, puntuaciones autodeclaradas y promesas de eludir detectores. |
| [blader/humanizer](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md) y [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) | Conservar los hechos y la voz que ya funciona, preferir la edición útil más pequeña, permitir `no_change` y no deducir que un texto fue escrito por IA a partir de una lista de patrones. | Fórmulas universales de voz y juicios automáticos sobre la autoría. |

## Perfiles de locale

Los perfiles son contratos de escritura nativa, no traducciones de las reglas del chino.

| Locale | Proyectos nativos y guías utilizados | Principios específicos adoptados |
| :--- | :--- | :--- |
| `zh-CN` | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) y [GB/T 15834-2011](https://openstd.samr.gov.cn/) | Sintaxis y terminología de China continental, puntuación de ancho completo, escritura extensa guiada por el material y reglas editoriales chinas limitadas a `zh-CN prose`. |
| `zh-TW` | [Guía de estilo zh-TW de Mozilla](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md) y [bruce6731/anti-ai-writing-taiwan](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | Vocabulario, registro y puntuación de Taiwán, reordenación cultural y el principio de que `zh-TW` no es una conversión de caracteres simplificados a tradicionales. No se importaron los términos específicos de los productos Mozilla. |
| `en` | [Google styleguide](https://github.com/google/styleguide/tree/gh-pages/docguide), [Microsoft Writing Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide) y [Digital.gov Plain Language](https://digital.gov/guides/plain-language/) | Relaciones claras entre actor y acción, documentación concisa, voz de marca contextual, coherencia regional y uso normal de la puntuación inglesa. No se importó la terminología específica de Microsoft. |
| `ja` | [Guía de estilo japonés de Mozilla](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md), [chezou/slop-nuki](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7), [iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2), [RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) y [coji/natural-japanese](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | Omisión y orden de palabras naturales, partículas, honoríficos y atenuación según el contexto, formas nominales o verbales según el componente, integridad de recursos de GUI y revisión sensible a la densidad y al género en lugar de prohibiciones absolutas de patrones. |
| `ko` | [Guía de estilo coreano de Mozilla](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md), [dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad) y [HarryJhin/korean-writing](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | Omisión natural del sujeto, partículas y espaciado, niveles de habla `합니다`/`해요`/`다`, conservación de honoríficos, terminaciones y calcos del inglés y el japonés. Se rechazaron las cuotas arbitrarias de reescritura. |
| `es` | [Guías de estilo en español de Mozilla](https://github.com/mozilla-l10n/styleguides/tree/main/docs/es) | Concordancia, clíticos, `tú`/`usted`/`ustedes`, interfaces con mayúsculas de tipo oración, terminología regional, puntuación y calcos del inglés. No se importaron las etiquetas específicas de Firefox ni un único registro universal para el español. |

Los proyectos enlazados conservan sus propias licencias. [Las notas de investigación](./research/multilingual-skill-research.md) documentan las fuentes y los límites de adopción; consulta la licencia de cada repositorio enlazado antes de reutilizar su texto o código. Las reglas de Humanization son resúmenes nuevos de los mecanismos anteriores.

## Instalación

Pídeselo a un agente que pueda instalar Skills desde GitHub:

```text
Instala la Skill humanization desde https://github.com/thevenomsnake/humanization. La Skill se encuentra en el directorio humanization/.
```

El directorio instalado debe conservar el nombre `humanization`. La tarjeta correcta se llama `Humanization`, usa un icono H verde oscuro con seis barras de idioma y muestra “Natural writing and GUI copy across six locales.” Si Codex muestra `活人感写作`, está enseñando la Skill antigua `human-writing`, no Humanization.

<details>
<summary><strong>Instalación manual</strong></summary>

Copia el directorio [`humanization`](./humanization) del repositorio en tu directorio de Skills de Codex:

```text
$CODEX_HOME/skills/humanization/
```

</details>

Úsala con un locale, formato y superficie explícitos:

```text
Usa $humanization con locale=ja, format=web-microcopy y surface=error. Reescribe estos mensajes de error sin alterar la CTA, los términos de marca, los placeholders ni la estructura del recurso de origen.
```

El nombre público de formato `web-microcopy` cubre textos de GUI en HTML, JSON, YAML, ARB, PO, código fuente y archivos de diseño. No se limita a sitios web.

Ejecuta el comprobador determinista con la misma selección explícita:

```bash
python humanization/scripts/check_writing.py --locale en --format copy draft.md
python humanization/scripts/check_writing.py --locale es --format web-microcopy --source source.json target.json
```

## Qué cambió en 3.0.0

- Se estableció `humanization` como nombre estable de la Skill y del directorio, con `Humanization` como nombre visible en la interfaz.
- Las instrucciones de ejecución se dividieron en un contrato común, seis perfiles de locale y un módulo de microcopy de GUI.
- Solo se adoptaron los principios textuales de `kill-ai-slop`; las reglas visuales sobre colores, tarjetas, esquinas, iconos y movimiento quedan fuera del alcance.
- `--locale` y `--format` pasaron a ser explícitos. El comprobador no adivina el idioma de textos mixtos ni convierte los juicios de tono en fallos bloqueantes.

Consulta [CHANGELOG.md](./CHANGELOG.md) para ver el historial completo.

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
| [`SKILL.md`](./humanization/SKILL.md) | Dirige cada tarea a través de los módulos común, de locale y de formato. |
| [`core.md`](./humanization/references/core.md) | Gestiona hechos, fuentes, capacidades, privacidad, CTA, términos de marca, placeholders y edición mínima. |
| [`locales/`](./humanization/references/locales) | Contiene los seis perfiles de escritura nativa. |
| [`expressive-text.md`](./humanization/references/formats/expressive-text.md) | Cubre textos no vinculados a una GUI: producto, documentación, marketing, correo electrónico y publicaciones sociales. |
| [`gui-microcopy.md`](./humanization/references/formats/gui-microcopy.md) | Define la función de los componentes de GUI y la protección de recursos estructurados. |
| [`check_writing.py`](./humanization/scripts/check_writing.py) | Proporciona una única CLI para las comprobaciones comunes, de locale y de GUI. |
| [`check_zh_cn.py`](./humanization/scripts/check_zh_cn.py) | Mantiene el comprobador original de acciones limitado a `zh-CN prose`. |

</details>

## Atribución y comentarios

Humanization se publica bajo la licencia MIT. El repositorio no incluye artículos de terceros, corpus de entrenamiento ni pesos de modelos.

Humanization es un proyecto independiente. Su base inicial de escritura extensa en `zh-CN` se derivó de [KKKKhazix/human-writing v1.1.0](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) bajo la licencia MIT. El mapa de fuentes anterior documenta todos los proyectos y guías que influyeron en la arquitectura actual, los principios adoptados de cada uno y las reglas específicas de cada proyecto que se excluyeron deliberadamente.

Para informar de conflictos entre reglas, falsos positivos o fallos específicos de un modelo, [abre una incidencia](https://github.com/thevenomsnake/humanization/issues) e incluye el prompt, la salida relevante y el resultado que esperabas.

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
