#!/bin/bash

PROM_DIR=~/SWE-4724_Team2_Project/owl-monitoring/prometheus
GRAF_DIR=~/SWE-4724_Team2_Project/owl-monitoring/grafana
NODE_EXPORTER_DIR=~/SWE-4724_Team2_Project/owl-monitoring/node_exporter
TEXTFILE_DIR=~/SWE-4724_Team2_Project/owl-monitoring/text-metrics

echo "🚀 Starting Prometheus..."
nohup $PROM_DIR/prometheus --config.file=$PROM_DIR/prometheus.yml > prometheus.log 2>&1 &

echo "📊 Starting Grafana..."
nohup $GRAF_DIR/bin/grafana-server --homepath=$GRAF_DIR web > grafana.log 2>&1 &

echo "📈 Starting Node Exporter with custom textfile collector..."
nohup $NODE_EXPORTER_DIR/node_exporter --collector.textfile.directory=$TEXTFILE_DIR > node_exporter.log 2>&1 &

echo "✅ Prometheus: http://localhost:9090"
echo "✅ Grafana:    http://localhost:3000 (user/pass: admin/admin)"
echo "✅ Node Exporter: http://localhost:9100/metrics"
