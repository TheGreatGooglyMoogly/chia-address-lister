import sqlite3

if __name__ == "__main__":
    sqlconn = sqlite3.connect('file:/home/USERNAME/.chia/mainnet/wallet/db/blockchain_wallet_v2_mainnet_CHALLENGE.sqlite?mode=ro', uri=True)
    try:
        cursor = sqlconn.execute("SELECT DISTINCT to_puzzle_hash FROM transaction_record ORDER BY created_at_time")
        for row in cursor:
            print(row[0])
    finally:
        sqlconn.close()
