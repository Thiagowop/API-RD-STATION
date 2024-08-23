import requests
from flask import current_app as app

# Detalhes da API do RD Station Marketing
rd_station_api_key = 'Chave rd station'
rd_station_company_endpoint = 'https://app.rdstation.com/api/v1/companies'
rd_station_contact_endpoint = 'https://app.rdstation.com/api/v1/contacts'

def transform_data_for_rd_station(data):
    transformed_data = []
    for record in data:
        customer_data = record['cliente']
        company_data = record['empresa']

        contact_payload = {
            'nome': customer_data['nome'],
            'email': customer_data['email'],
            'telefone': customer_data['telefone'],
            'cargo': customer_data['cargo'],
            'company_id': company_data['id']
        }

        company_payload = {
            'nome': company_data['nome'],
            'segmento': company_data['segmento'],
            'segmento_secundario': company_data['segmento_secundario']
        }

        transformed_data.append({
            'contato': contact_payload,
            'empresa': company_payload
        })

    return transformed_data

def integrate_data_into_rd_station(data):
    headers = {
        'Authorization': f'Bearer {rd_station_api_key}',
        'Content-Type': 'application/json'
    }

    for record in data:
        contact_payload = record['contato']
        company_payload = record['empresa']

        try:
            contact_id = contact_payload.get('id')
            if contact_id:
                contact_url = f'{rd_station_contact_endpoint}/{contact_id}'
                response = requests.put(contact_url, json=contact_payload, headers=headers)
            else:
                response = requests.post(rd_station_contact_endpoint, json=contact_payload, headers=headers)
            
            if response.status_code not in [200, 201]:
                app.logger.error(f"Falha ao integrar contato: {response.status_code} - {response.text}")

            company_id = company_payload.get('id')
            if company_id:
                company_url = f'{rd_station_company_endpoint}/{company_id}'
                response = requests.put(company_url, json=company_payload, headers=headers)
            else:
                response = requests.post(rd_station_company_endpoint, json=company_payload, headers=headers)

            if response.status_code not in [200, 201]:
                app.logger.error(f"Falha ao integrar empresa: {response.status_code} - {response.text}")

        except Exception as e:
            app.logger.error(f"Erro ao integrar dados no RD Station: {e}")
