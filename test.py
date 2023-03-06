def conn_prob_model(adj_matrix, nrn_table, **kwargs):
    """General probability model building, optionally for multiple random subsets of neurons.

    Parameters
    ----------
    adj_matrix : array_like
        Adjacency matrix of the circuit
    nrn_table : dataframe
        Pandas dataframe with information about neurons
    **kwargs : dict, optional
        Extra arguments to pass to function

    Returns
    -------
    array_like
        A new adjacency matrix


    Examples
    --------
    A comment explaining this example.

    >>> adj = np.array([0,1,1],[0,0,1],[0,0,0])
    >>> df = pd.read_pickle('nrn_table.pkl')
    >>> conn_prob_model(adj, df)
    np.array([[0,0,0],[1,0,0],[1,1,0]])


    Raises
    ------
    KeyError
        If the dataframe is missing information about neurons

    See Also
    --------
    conn_prob_2nd_order_model : Same, specified to 2nd order

    Notes
    -----
    An insightful math comment:

    .. math:: \Sum_{i=1}^\infty K_i+\frac{4}{i}

    References
    ----------
    .. [1] Author A, Author B, "Title," Journal, volume, pages, year.




    """
