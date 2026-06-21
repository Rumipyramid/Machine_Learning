/* Construye explorador_standalone.html inyectando engine.js dentro de index.html,
 * para tener la app en un único archivo portable.
 * Uso:  node build_standalone.js
 */
const fs = require("fs");
const path = require("path");
const dir = __dirname;
const engine = fs.readFileSync(path.join(dir, "engine.js"), "utf8");
let html = fs.readFileSync(path.join(dir, "index.html"), "utf8");
html = html.replace('<script src="engine.js"></script>', "<script>\n" + engine + "\n</script>");
fs.writeFileSync(path.join(dir, "explorador_standalone.html"), html);
console.log("OK -> explorador_standalone.html (" + html.length + " bytes)");
