monto_deuda = float(2170549.90)
tasa = float(2.5)
divisor1 = float(0.99625)
divisor2 = float(0.9975)
alicuota = int(20)

sellado_eng = round((monto_deuda/divisor1)+ alicuota - monto_deuda,2)
sellado_sfb = round((monto_deuda/divisor2)+ alicuota - monto_deuda,)


print(f"Engage: {sellado_eng} SFB: {sellado_sfb}")