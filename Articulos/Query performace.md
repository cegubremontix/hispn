Algunas recomendaciones de optimizar consultas SQL
 
No hay receta unica para optmizar queries.
 
1. Crear indices para columnas mas usados  - Por defecto b-tree, no son unicos.
 
2. Que es el costo? Como se mide el costo de un plan de ejecucion? / Cantidad fisica adimensional
 
Plan de Ejecución:
- Cardinalidad: Numero de elementos en un conjunto.
 
3. Evitar el uso del like.
 
4. No utilize el operator UNION si el objeto se puedo lograr a travez del UNION ALL, UNION incurre en una operacion de ordenamiento extra que se puede evitar.
 
5. Seleccionar solo las columanas requeridas . No select * from ...
 
6. No emplear el DISTINCT si el objetivo se puede lograr de otra forma.
 
7. Cuando se utilizan varias tablas, acceda a las columnas siempre utilizando un alias o utilizando el nombre completo de la tabla (tabla.columna). No deja trabajo de resolver la referencias de los nombrs de las columnas.
 
8. Utilizar alias significativos para tablas/vitas.
 
9. A escribir sub-consultas ejecutar (exists) vs (in).
 
10. NO utilizar funciones RTRIM, TO_CHAR, UPPER, TRUNC en columnas que forman parte de un indice, esto evitara que el optmizar identifique el indice.  Index by function.
 
11. Evitar los siguientes de expressiones complejas: NVL, TO_DATE, TO_NUMBER, y asi sucesivamente.
Estas expresiones impiden que el optmizador asigne estimaciones de cardinalidad o puede affectar al plan general  y al método de combinación.
 
12. Siempre es mejor escribir instrucciones SQL separadas para diferentes tareas, pero si debe usar una sentencia SQL, puede hacer una declaración un poco menos compleja utilizando el operator UNION ALL.
 
13. No se recomiendan combinaciones a vistas complejas, en particular las combinaciones de uan vista compleja a otro eso hace que la vista compelta se  instancie, y la consulta se ejecutara contra los datatos de la vista.
