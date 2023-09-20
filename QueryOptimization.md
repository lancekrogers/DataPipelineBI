## Query 1
```sql
SELECT t.*, b.balance
FROM transfers t
JOIN balance b ON t."toAddress" = b.walletAddress
WHERE b.balance > 1000
AND t.contractAddress = 'some_contract_address';
```
### Optimizations
- Select only the required columns instead of selecting *
- Add indexes to toAddress, walletAddress and contractAddress

## Queury 2
```sql
SELECT DISTINCT "toAddress", contract_address
FROM transfers
WHERE contract_address IN ('address1', 'address2', 'address3');
```
### Optimizations
- Add indexes to contract_address and toAddress
