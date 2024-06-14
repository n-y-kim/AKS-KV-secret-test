# AKS-KV-secret-test

## Network Policy 구성

- Deny all Ingress/Egress
- Allow **KeyVault private ip address** & **Managed Identity server public ip**
- Allow Azure DNS setting
- Allow `login.microsoft.com` ipv4

## 테스트 앱 구성
- `kv-test.py`: `DefaultAzureCredential` & KeyVault SDK로 secret 값 회수 & 값 print

## Flow
Network Policy의 정책 때문에 특정 pod(예; kv-app)에서만 KeyVault에 접근할 수 있게 됨. 이때 Keyvault에 authentication하기 위해 Managed Identity에서 토큰 회수. Managed Identity에 할당된 RBAC으로 autorization 완료.
