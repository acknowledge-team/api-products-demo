from django.http import JsonResponse
import json

def index(request):
  """
  Return JsonResponse object
  This view is used for / uri.
  It returns a json containing hashicorp product information
  """
  data = [
    {
      'name': 'consul',
      'description': 'Connect and secure your apps with service mesh',
      'vendor': 'hashicorp'
    },
    {
      'name': 'nomad',
      'description': 'Orchestrate your workloads',
      'vendor': 'hashicorp'
    },
    {
      'name': 'terraform',
      'description': 'Provision your infrastructure as code and gouvern',
      'vendor': 'hashicorp'
    },
    {
      'name': 'Vault',
      'description': 'Secure application secrets and provide encryption as service',
      'vendor': 'hashicorp'
    }
  ]
  response = JsonResponse(data, safe=False)
  return(response)
