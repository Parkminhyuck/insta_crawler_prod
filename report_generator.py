
import pandas as pd
import os

def generate_report(csv_path="logs/processed_accounts.csv", output_path="logs/dm_report.xlsx"):
    if not os.path.exists(csv_path):
        print("❌ CSV 로그 파일이 존재하지 않습니다.")
        return

    df = pd.read_csv(csv_path, names=["uid", "grade", "followers", "likes", "status"])
    df = df[df["status"] == "성공"]

    # 등급별 DM 전송 수
    grade_counts = df["grade"].value_counts().sort_index()

    # 팔로워 평균
    avg_followers = df["followers"].mean()
    avg_likes = df["likes"].mean()

    with pd.ExcelWriter(output_path) as writer:
        df.to_excel(writer, sheet_name="DM Success Raw", index=False)

        summary = pd.DataFrame({
            "등급": grade_counts.index,
            "DM 성공 수": grade_counts.values
        })
        summary.to_excel(writer, sheet_name="요약", index=False)

        stats = pd.DataFrame({
            "지표": ["팔로워 평균", "좋아요 평균", "총 DM 성공 수"],
            "값": [round(avg_followers, 1), round(avg_likes, 1), len(df)]
        })
        stats.to_excel(writer, sheet_name="지표 통계", index=False)

    print(f"📊 보고서 생성 완료 → {output_path}")

if __name__ == "__main__":
    generate_report()
