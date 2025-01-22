from django.shortcuts import render
from .models import Gasto, Departamento
from django.db.models import Sum

def gastos_view(request):
    gastos = Gasto.objects.all()
    return render(request, "gastos.html", {"gastos": gastos})

def filtrado_view(request):
    resultados = None
    if request.method == "POST":
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")

        if fecha_inicio and fecha_fin:
            resultados = (
                Gasto.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
                .values("departamento__nombre")
                .annotate(total=Sum("monto"))
                .order_by("departamento__nombre")
            )

    return render(request, "filtrado.html", {"resultados": resultados})