# main.py

from coleccionPendientes import ColeccionPendientes
from coleccionEnProceso import ColeccionEnProceso
from coleccionTerminado import ColeccionTerminados

def main():
    # Crear una instancia de ColeccionPendientes
    cp = ColeccionPendientes()

    # Insertar los pendientes con títulos y descripciones
    cp.insertar("Desarrollo de Aplicación Móvil de Salud", "Este proyecto implica la creación de una aplicación móvil orientada a la salud que permita a los usuarios monitorear sus signos vitales como el ritmo cardíaco, la presión arterial y la actividad física. Además de la monitorización, la app proporcionará recomendaciones personalizadas sobre hábitos saludables basados en los datos recopilados.")
    cp.insertar("Investigación de Mercado para Nuevo Producto", "Esta iniciativa consiste en realizar un estudio exhaustivo del mercado para evaluar la demanda y la aceptación potencial de un nuevo producto tecnológico. El objetivo es comprender las necesidades del mercado objetivo y identificar oportunidades para posicionar eficazmente el producto.")
    cp.insertar("Diseño de Campaña de Marketing Digital", "Este proyecto implica la creación de una campaña integral de marketing digital para aumentar la visibilidad de la marca en plataformas digitales. Se centrará en mejorar la generación de leads, aumentar la interacción en redes sociales y mejorar las conversiones.")

    # Crear una instancia de ColeccionEnProceso
    cep = ColeccionEnProceso()

    # Insertar los en proceso con títulos y descripciones
    cep.insertar("Implementación de Sistema ERP", "Este proyecto se centra en la implementación de un sistema ERP (Enterprise Resource Planning) para integrar y optimizar procesos empresariales. El objetivo es mejorar la eficiencia operativa, la gestión de recursos y la toma de decisiones estratégicas.")
    cep.insertar("Rediseño de Sitio Web Corporativo", "Este proyecto implica el rediseño completo del sitio web corporativo para mejorar la experiencia del usuario, la funcionalidad y el rendimiento SEO. Se enfoca en actualizar la estética visual y optimizar la navegación para aumentar la conversión y la retención de usuarios.")
    cep.insertar("Desarrollo de Curso Online de Programación", "Este proyecto consiste en crear un curso completo de programación en línea, centrado en el desarrollo web. El objetivo es proporcionar contenido educativo interactivo y de alta calidad que abarque desde principiantes hasta niveles avanzados.")

    # Crear una instancia de ColeccionTerminados
    ct = ColeccionTerminados()

    # Insertar los terminados con títulos y descripciones
    ct.insertar("Lanzamiento de Producto Innovador", "Este proyecto culminó con el exitoso lanzamiento de un dispositivo IoT para hogares inteligentes en el mercado nacional. El producto ofrece funciones avanzadas de automatización del hogar y conectividad inteligente.")
    ct.insertar("Implementación de Programa de Sostenibilidad", "Este proyecto incluyó la implementación de un programa integral de sostenibilidad empresarial. Se centró en la reducción de la huella de carbono, la gestión eficiente de recursos y la promoción de prácticas comerciales responsables.")
    ct.insertar("Organización de Evento Corporativo Anual", "Este proyecto abarcó la planificación y ejecución exitosa de un evento corporativo anual, que incluyó conferencias, talleres y actividades de networking para más de 500 asistentes.")

    # Mostrar que los títulos y descripciones han sido insertados
    print("Títulos y descripciones insertados exitosamente.")

if __name__ == "__main__":
    main()
