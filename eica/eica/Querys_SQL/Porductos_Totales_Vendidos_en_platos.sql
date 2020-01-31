SELECT
boleta_venta_restaurante.id AS "id_boleta_restaurante",
plato_hijo_venta.id AS "id_plato_hijo_venta",
plato_hijo_venta.cantidad AS "cantidad_plato_hijo_venta",
producto_plato.id_plato_padre,
plato_padre.nombre,
producto_plato.id_producto_padre,
producto_plato.cantidad,
producto_padre.nombre,
producto_padre.unidad,
plato_hijo_venta.cantidad * producto_plato.cantidad as cantidad_producto_consumido
FROM plato_hijo_venta 
INNER JOIN plato_padre ON plato_hijo_venta.id_plato_padre=plato_padre.id
INNER JOIN producto_plato ON producto_plato.id_plato_padre = plato_padre.id
INNER JOIN producto_padre ON producto_padre.id = producto_plato.id_producto_padre
INNER JOIN boleta_venta_restaurante ON boleta_venta_restaurante.id = plato_hijo_venta.id_boleta_venta_restaurante



