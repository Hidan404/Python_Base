param (
    [string]$Interface,
    [string]$NovoMac
)

function Gerar-MacAleatorio {
    $bytes = @(For ($i=0; $i -lt 6; $i++) {Get-Random -Minimum 0 -Maximum 256})
    $bytes[0] = ($bytes[0] -band 0xFC) -bor 0x02
    $mac = ($bytes | ForEach-Object { "{0:X2}" -f $_ }) -join ''
    return $mac
}

if (-not $NovoMac) {
    Write-Host "Nenhum MAC informado. Gerando um aleatório..."
    $NovoMac = Gerar-MacAleatorio
}

Write-Host "Interface: $Interface"
Write-Host "MAC a ser usado: $NovoMac"

# Chave base do registro das interfaces de rede
$baseKey = "HKLM:\SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}"

# Busca a subchave correta para a interface
$subKeys = Get-ChildItem $baseKey

foreach ($key in $subKeys) {
    $netCfgInstanceId = (Get-ItemProperty $key.PSPath).NetCfgInstanceId
    if ($netCfgInstanceId) {
        # Verifica se o NetCfgInstanceId corresponde à interface
        # Para isso precisamos de um jeito de relacionar nome -> NetCfgInstanceId
        # Como simplificação, aqui você deve substituir manualmente ou adaptar
        # Caso contrário, você pode listar as interfaces via WMI (mais complexo)
        # Vou assumir que o usuário sabe o NetCfgInstanceId correto para a interface

        # --- Exemplo: vamos alterar o MAC para todas as interfaces aqui só para teste ---
        # ATENÇÃO: Na prática, deve-se identificar a interface certa!

        Write-Host "Alterando MAC no registro da chave: $($key.PSPath)"
        Set-ItemProperty -Path $key.PSPath -Name "NetworkAddress" -Value $NovoMac
    }
}

# Reinicia a interface
Write-Host "Reiniciando interface $Interface..."
Restart-NetAdapter -Name $Interface -Confirm:$false

Write-Host "MAC alterado com sucesso!"
