import pytest
from app import app, db, Respuesta

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

# 1. Página de inicio (formulario empleado)
def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Nombre" in response.data

# 2. Envío del formulario empleado
def test_post_empleado(client):
    response = client.post('/', data={
        'nombre': 'Prueba',
        'apellido': 'Test',
        'vivienda': 'Casa',
        'departamento': 'Antioquia',
        'estado_civil': 'soltero',
        'genero': 'masculino',
        'edad': '30',
        'salario': '3000000',
        'cargo': 'Desarrollador',
        'estrato': '3'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"relaciones" in response.data  # Llega al formulario de Amor

# 3. Ver respuestas guardadas
def test_ver_respuestas(client):
    response = client.get('/ver_respuestas')
    assert response.status_code == 200
    assert b"Respuestas Guardadas" in response.data

# 4. Descargar CSV
def test_descargar_csv(client):
    client.get('/exportar_csv')  # Exportar primero
    response = client.get('/descargar_csv')
    assert response.status_code == 200
    assert response.mimetype == 'text/csv'
    assert 'attachment; filename=respuestas.csv' in response.headers['Content-Disposition']

def test_eliminar_respuesta(client):
    # Crear una respuesta de prueba dentro del contexto
    with app.app_context():
        nueva = Respuesta(
            formulario="empleado",
            nombre="Eliminar",
            apellido="Test",
            edad=25
        )
        db.session.add(nueva)
        db.session.commit()
        respuesta_id = nueva.id

    # Confirmar que la respuesta existe
    with app.app_context():
        assert Respuesta.query.get(respuesta_id) is not None

    # Eliminar usando el cliente
    response = client.post(f'/eliminar_respuesta/{respuesta_id}', follow_redirects=True)
    assert response.status_code == 200

    # Confirmar que ya no existe
    with app.app_context():
        assert Respuesta.query.get(respuesta_id) is None
