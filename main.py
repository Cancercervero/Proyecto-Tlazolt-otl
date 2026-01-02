import argparse
import sys
import os

# Add src to path just in case
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.simulacion_torre import TlazolteotlSimulator

def main():
    parser = argparse.ArgumentParser(description="Proyecto Tlazoltéotl: Urban Terraforming System Controller")
    
    parser.add_argument('--run-sim', action='store_true', help="Run the basic particle capture simulation")
    parser.add_argument('--real-data', action='store_true', help="Use real CDMX data for the simulation")
    parser.add_argument('--gen-history', action='store_true', help="Generate and analyze year-long 2026 history")
    parser.add_argument('--plot-history', action='store_true', help="Generate multi-scale validation graphs")
    parser.add_argument('--poster', action='store_true', help="Generate the final Engineering Master Sheet")
    parser.add_argument('--all', action='store_true', help="Run the entire pipeline")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    if args.run_sim or args.all:
        mode = "cdmx_real" if args.real_data else "simulated"
        sim = TlazolteotlSimulator(mode=mode)
        sim.run()
        sim.report()
        # Note: sim.plot() is available but usually we want headless for pipeline
        if args.run_sim and not args.all:
            sim.plot()

    if args.gen_history or args.all:
        import src.analisis_historico as ah
        print("\n📈 Running Year-Long Historical Analysis...")
        datos = ah.simular_datos_historicos_2026()
        rendimiento = ah.calcular_rendimiento_torre(datos)
        ah.agregar_por_periodo(datos, datos['fechas'], rendimiento)
        # Result saved to JSON in the script itself

    if args.plot_history or args.all:
        print("\n📊 Generating Validation Graphs...")
        # Since the script is mostly top-level code, we run it
        import src.graficar_historico
        
    if args.poster or args.all:
        print("\n🎨 Assembling Engineering Master Sheet...")
        from src.generar_poster import crear_poster
        crear_poster()

    print("\n✅ Task completed successfully.")

if __name__ == "__main__":
    main()
