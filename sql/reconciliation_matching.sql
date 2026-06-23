SELECT
    s.transaction_id,
    s.amount AS settlement_amount,
    g.amount AS gl_amount,

    CASE
        WHEN g.transaction_id IS NULL
            THEN 'UNMATCHED'

        WHEN s.amount <> g.amount
            THEN 'AMOUNT_VARIANCE'

        WHEN DATE(s.posting_date) <>
             DATE(g.posting_date)
            THEN 'TIMING_DIFFERENCE'

        ELSE 'MATCHED'
    END AS status

FROM settlement_transactions s
LEFT JOIN gl_transactions g
ON s.transaction_id = g.transaction_id;
