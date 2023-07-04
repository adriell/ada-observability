from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
import logging

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/renda-fixa')
@metrics.counter('vendas_renda_fixa', 'Numero de acoes de renda fixas efetivados', labels={'tipo':'ACOES'})
def renda_fixa():
    return render_template("lista.html", titulo="Renda Fixa")
@app.route('/renda-variavel')
@metrics.counter('vendas_renda_variavel', 'Numero de acoes de renda variável efetivados', labels={'tipo':'VARIAVEL'})
def renda_variavel():
    return render_template("lista.html", titulo="Renda Fixa")
if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    app.run(host="0.0.0.0", port=5001)