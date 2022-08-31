def definition_is_dictionary(table_def: dict):
    """Ensure the definition is a dictionary"""
    # The definition must:
    # 1. Be a dictionary
    assert type(table_def) == dict

def definition_has_valid_name(table_def: dict):
    """Ensure the definition has a valid name"""
    # The definition must:
    # 1. Have a key called 'name'
    assert 'name' in table_def.keys()
    # 2. The name must be a string
    assert type(table_def['name']) == str
    # 3. The name must contain at least one character
    assert len(table_def['name']) > 0

def definition_has_valid_columns(table_def: dict):
    """Ensure the definition has valid column names"""
    # The definition must:
    # 1. Have a key called 'columns'
    assert 'columns' in table_def.keys()
    # 2. Contain a list under the 'columns' key
    assert type(table_def['columns']) == list
    # 3. Define at least one column name
    assert len(table_def['columns']) > 0
    # 4. Have all column names be at least one character long
    for v in table_def['columns']:
        assert len(v) > 0
    # 5. Have all column names capitalized
    for v in table_def['columns']:
        assert v[0].isupper() == True

def definition_has_valid_affinities(table_def: dict):
    """Ensure the definition has valid affinities"""
    # The definition must:
    # 1. Have a key called 'affinities'
    assert 'affinities' in table_def.keys()
    # 2. Contain a list under the 'affinities' key
    assert type(table_def['affinities']) == list
    # 3. Define at least one column name
    assert len(table_def['affinities']) > 0
    # 4. Contain only affinities from the following list:
    # TEXT, NUMERIC, INTEGER, REAL, BLOB
    for v in table_def['affinities']:
        assert v in ['TEXT', 'NUMERIC', 'INTEGER', 'REAL', 'BLOB']

def definition_has_equal_length_columns_and_affinities(table_def: dict):
    """Ensure the definiton has an equal number of columns and affinities"""
    assert len(table_def['columns']) == len(table_def['affinities'])
