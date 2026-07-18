import pandas as pd
import numpy as np

# ------------------------------------------------------------
# 1. BASE DE DADOS (gerando os 50 produtos)
# ------------------------------------------------------------

# Garantindo mais de 50 nomes para não repetir com replace=False
nomes_produtos = [
    'Smartphone', 'Notebook', 'Fone de Ouvido', 'Monitor', 'Teclado',
    'Camiseta', 'Calça Jeans', 'Tênis', 'Jaqueta', 'Vestido',
    'Livro de Ficção', 'Livro de Autoajuda', 'Livro Técnico', 'HQ', 'Mangá',
    'Sofá', 'Mesa', 'Cadeira', 'Estante', 'Luminária',
    'Bola de Futebol', 'Raquete', 'Tênis de Corrida', 'Bicicleta', 'Halter',
    'Shampoo', 'Condicionador', 'Perfume', 'Maquiagem', 'Creme Facial',
    'Boneca', 'Carrinho', 'Quebra-cabeça', 'Jogo de Tabuleiro', 'Videogame',
    'Óleo de Motor', 'Bateria', 'Pneu', 'Kit Ferramentas', 'Capa de Banco',
    'Mouse', 'Headset', 'Webcam', 'Roteador', 'HD Externo',
    'Café', 'Chá', 'Refrigerante', 'Suco', 'Cerveja', 'Vinho',
    'Micro-ondas', 'Geladeira', 'Fogão', 'Lavadora', 'Aspirador'
]

categorias = [
    'Eletrônicos', 'Vestuário', 'Livros', 'Casa & Decoração',
    'Esportes', 'Beleza & Cuidados', 'Brinquedos', 'Automotivo',
    'Informática', 'Alimentos', 'Bebidas', 'Jardinagem'
]

# Criando o DataFrame
data = {
    'id': range(1, 51),
    'nome': np.random.choice(nomes_produtos, size=50, replace=False),
    'preco': np.round(np.random.uniform(10, 2000, 50), 2),
    'categoria': np.random.choice(categorias, size=50),
    'avaliacao': np.round(np.random.uniform(1, 5, 50), 1)
}

df = pd.DataFrame(data)
df = df[['id', 'nome', 'preco', 'categoria', 'avaliacao']]

print("="*60)
print("DATAFRAME GERADO (primeiras 5 linhas)")
print("="*60)
print(df.head())
print("\n")

# ------------------------------------------------------------
# 2. INSPEÇÃO E INFORMAÇÕES GERAIS
# ------------------------------------------------------------
print("="*60)
print("2. INSPEÇÃO E INFORMAÇÕES GERAIS")
print("="*60)

# shape: retorna uma tupla (linhas, colunas)
print(f"Shape (linhas, colunas): {df.shape}")

# info(): mostra tipos de dados e contagem de valores não nulos
print("\nInfo do DataFrame:")
print(df.info())

# describe(): estatísticas descritivas das colunas numéricas
print("\nEstatísticas descritivas (preço e avaliação):")
print(df[['preco', 'avaliacao']].describe())

# columns: lista os nomes das colunas
print(f"\nColunas: {df.columns.tolist()}")

# dtypes: mostra o tipo de cada coluna
print(f"\nTipos de dados:\n{df.dtypes}")

# ------------------------------------------------------------
# 3. SELEÇÃO E INDEXAÇÃO
# ------------------------------------------------------------
print("\n" + "="*60)
print("3. SELEÇÃO E INDEXAÇÃO")
print("="*60)

# Selecionar uma coluna (retorna Series)
print("Coluna 'nome' (primeiros 3):")
print(df['nome'].head(3))

# Selecionar múltiplas colunas (retorna DataFrame)
print("\nColunas 'id' e 'preco' (primeiros 3):")
print(df[['id', 'preco']].head(3))

# loc[]: seleciona por rótulo do índice (linhas e colunas)
print("\nUsando loc - linha 0 e colunas 'nome' e 'categoria':")
print(df.loc[0, ['nome', 'categoria']])

# iloc[]: seleciona por posição (linha 0, coluna 1)
print("\nUsando iloc - primeira linha, segunda coluna (índice 1):")
print(df.iloc[0, 1])  # equivalente ao 'nome'

# Slicing com iloc (linhas 0 a 4, colunas 0 a 2)
print("\nSlicing com iloc (linhas 0-4, colunas 0-2):")
print(df.iloc[0:5, 0:3])

# ------------------------------------------------------------
# 4. FILTRAGEM DE DADOS (BOOLEAN INDEXING)
# ------------------------------------------------------------
print("\n" + "="*60)
print("4. FILTRAGEM DE DADOS")
print("="*60)

# Filtro simples: categoria igual a "Livros"
print("Produtos da categoria 'Livros':")
print(df[df['categoria'] == 'Livros'])

# Filtro com múltiplas condições usando & (E) e | (OU)
# SEMPRE use parênteses em cada condição
print("\nProdutos com preço entre 900 e 1500 (usando &):")
filtro_preco = (df['preco'] > 900) & (df['preco'] < 1500)
print(df[filtro_preco])

# Alternativa mais simples: between()
print("\nProdutos com preço entre 900 e 1500 (usando between):")
print(df[df['preco'].between(900, 1500)])

# Filtro combinando categoria E preço
print("\nProdutos da 'Informática' com preço > 950:")
filtro_composto = (df['categoria'] == 'Informática') & (df['preco'] > 950)
print(df[filtro_composto])

# Filtro com OU (|) - produtos de 'Livros' OU com avaliação > 4.8
print("\nProdutos 'Livros' OU com avaliação > 4.8:")
filtro_ou = (df['categoria'] == 'Livros') | (df['avaliacao'] > 4.8)
print(df[filtro_ou])

# Filtro com isin() - categorias específicas
print("\nProdutos das categorias 'Eletrônicos' ou 'Informática':")
print(df[df['categoria'].isin(['Eletrônicos', 'Informática'])])

# Filtro com negação (~) - tudo que NÃO for da categoria 'Brinquedos'
print("\nProdutos que NÃO são da categoria 'Brinquedos':")
print(df[~df['categoria'].isin(['Brinquedos'])])

# query() - forma alternativa de filtrar com sintaxe SQL-like
print("\nUsando query - preço > 1000 e avaliação >= 4.5:")
print(df.query('preco > 1000 and avaliacao >= 4.5'))

# ------------------------------------------------------------
# 5. ORDENAÇÃO (SORT)
# ------------------------------------------------------------
print("\n" + "="*60)
print("5. ORDENAÇÃO")
print("="*60)

# Ordenar por preço (crescente)
print("Top 5 produtos mais baratos:")
print(df.sort_values('preco').head(5))

# Ordenar por preço (decrescente) e avaliação (crescente)
print("\nTop 5 produtos mais caros (ordenado por preço desc, avaliação asc):")
print(df.sort_values(['preco', 'avaliacao'], ascending=[False, True]).head(5))

# ------------------------------------------------------------
# 6. ANÁLISE ESTATÍSTICA E AGREGAÇÕES
# ------------------------------------------------------------
print("\n" + "="*60)
print("6. ANÁLISE ESTATÍSTICA E AGREGAÇÕES")
print("="*60)

# Média, soma, máximo, mínimo de uma coluna
print(f"Média de preços: R$ {df['preco'].mean():.2f}")
print(f"Soma total dos preços: R$ {df['preco'].sum():.2f}")
print(f"Preço máximo: R$ {df['preco'].max():.2f}")
print(f"Preço mínimo: R$ {df['preco'].min():.2f}")
print(f"Desvio padrão do preço: {df['preco'].std():.2f}")
print(f"Mediana do preço: {df['preco'].median():.2f}")

# value_counts() - contagem de frequência (categorias)
print("\nQuantidade de produtos por categoria:")
print(df['categoria'].value_counts())

# value_counts() com porcentagem
print("\nPorcentagem de produtos por categoria:")
print(df['categoria'].value_counts(normalize=True) * 100)

# ------------------------------------------------------------
# 7. GROUPBY (AGRUPAMENTO)
# ------------------------------------------------------------
print("\n" + "="*60)
print("7. GROUPBY - AGRUPAMENTO DE DADOS")
print("="*60)

# Agrupar por categoria e calcular a média do preço
print("Preço médio por categoria:")
print(df.groupby('categoria')['preco'].mean().round(2))

# Várias agregações ao mesmo tempo
print("\nEstatísticas por categoria (média, máximo e contagem):")
agregacoes = df.groupby('categoria').agg({
    'preco': ['mean', 'max', 'count'],
    'avaliacao': ['mean', 'min']
})
print(agregacoes.round(2))

# Encontrar o produto mais caro de cada categoria (usando idxmax)
print("\nProduto mais caro de cada categoria:")
idx_caros = df.groupby('categoria')['preco'].idxmax()
print(df.loc[idx_caros, ['categoria', 'nome', 'preco']])

# ------------------------------------------------------------
# 8. CRIAÇÃO E MODIFICAÇÃO DE COLUNAS
# ------------------------------------------------------------
print("\n" + "="*60)
print("8. CRIAÇÃO E MODIFICAÇÃO DE COLUNAS")
print("="*60)

# Criando uma nova coluna: 'desconto' (10% do valor)
df['desconto'] = df['preco'] * 0.10
print("Coluna 'desconto' adicionada (primeiras 3):")
print(df[['nome', 'preco', 'desconto']].head(3))

# Criando coluna com condição: 'faixa_preco' (Baixo, Médio, Alto)
def classificar_preco(valor):
    if valor < 300:
        return 'Baixo'
    elif valor < 1000:
        return 'Médio'
    else:
        return 'Alto'

df['faixa_preco'] = df['preco'].apply(classificar_preco)
print("\nColuna 'faixa_preco' criada (primeiras 3):")
print(df[['nome', 'preco', 'faixa_preco']].head(3))

# Usando apply com lambda para criar coluna 'preco_com_desconto'
df['preco_com_desconto'] = df.apply(lambda row: row['preco'] - row['desconto'], axis=1)
print("\nColuna 'preco_com_desconto' criada (primeiras 3):")
print(df[['nome', 'preco', 'desconto', 'preco_com_desconto']].head(3))

# Renomear colunas
df_renomeado = df.rename(columns={'nome': 'produto', 'preco': 'valor'})
print("\nRenomeando colunas 'nome' -> 'produto' e 'preco' -> 'valor':")
print(df_renomeado.columns.tolist())

# Remover colunas (drop)
df_sem_temp = df.drop(columns=['desconto', 'faixa_preco', 'preco_com_desconto'])
print("\nColunas removidas (desconto, faixa_preco, preco_com_desconto). Colunas atuais:")
print(df_sem_temp.columns.tolist())

# ------------------------------------------------------------
# 9. TRATAMENTO DE DADOS FALTANTES (NULOS)
# ------------------------------------------------------------
print("\n" + "="*60)
print("9. TRATAMENTO DE DADOS FALTANTES")
print("="*60)

# Criando uma cópia para testar (introduzindo um valor nulo)
df_com_nulo = df.copy()
df_com_nulo.loc[0, 'avaliacao'] = np.nan  # Forçando um NaN

# Verificar valores nulos
print(f"Valores nulos por coluna:\n{df_com_nulo.isnull().sum()}")

# Preencher nulos com a média da coluna
df_com_nulo['avaliacao'] = df_com_nulo['avaliacao'].fillna(df_com_nulo['avaliacao'].mean())
print(f"\nApós preencher nulo com a média ({df_com_nulo.loc[0, 'avaliacao']:.2f}):")
print(df_com_nulo.head(1)[['nome', 'avaliacao']])

# Outra forma: dropar linhas com nulos (dropna)
# df_sem_nulos = df.dropna()

# ------------------------------------------------------------
# 10. OPERAÇÕES DE JUNÇÃO (MERGE / CONCAT)
# ------------------------------------------------------------
print("\n" + "="*60)
print("10. JUNÇÃO (MERGE / CONCAT)")
print("="*60)

# Criando um segundo DataFrame com estoque
df_estoque = pd.DataFrame({
    'id': [1, 3, 5, 10, 25],
    'estoque': [50, 30, 20, 10, 5]
})
print("Tabela de Estoque (parcial):")
print(df_estoque)

# Merge (JOIN) - trazendo as informações de estoque para o df principal
df_completo = pd.merge(df, df_estoque, on='id', how='left')
print("\nMerge LEFT JOIN (traz estoque, deixa NaN onde não tem):")
print(df_completo[['id', 'nome', 'estoque']].head(10))

# Concatenação de DataFrames (empilhar linhas)
print("\nConcatenando verticalmente (adicionando 2 produtos fictícios):")
novos_produtos = pd.DataFrame({
    'id': [51, 52],
    'nome': ['Drone', 'Tablet'],
    'preco': [1200.00, 850.00],
    'categoria': ['Eletrônicos', 'Informática'],
    'avaliacao': [4.9, 4.7]
})
df_concatenado = pd.concat([df, novos_produtos], ignore_index=True)
print(f"Shape original: {df.shape} -> Shape após concat: {df_concatenado.shape}")

print("\n" + "="*60)
print("FIM DAS OPERAÇÕES!")
print("="*60) 