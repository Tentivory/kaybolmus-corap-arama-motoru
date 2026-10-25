#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kaybolmuş Çorap Arama Motoru v0.1
Bu program çorapları asla bulmaz. Bulursa bu bir bug'dır.
"""

import random
import time
import sys

def corap_ara():
    print("\U0001f9e6 Çorap arama motoru başlatılıyor...")
    time.sleep(1)
    
    bahane_listesi = [
        "Çorap çamaşır makinesinin arkasına kaçmış, orada yaşıyor artık.",
        "Eşiyle kavga etmiş, tek başına yurtdışına gitmiş.",
        "Çorap aslında hiç var olmamış, sen hayal görmüşsün.",
        "Kuantum tünelinden geçip paralel evrene kaçmış.",
        "Çorap sendikaya üye olmuş, grevde.",
        "Annesi onu çağırmış, köye dönmüş."
    ]
    
    for i in range(5):
        print(f"Aranıyor... {i+1}/5")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"⚠️  {random.choice(bahane_listesi)}")
    
    print("\n❌ Çorap bulunamadı. Özür dileriz, sistem tasarımı gereği bulamaz.")
    print("💡 Öneri: Yeni çorap al. Eski çoraplar zaten eşsizdi.")
    
    # Gizli mesaj: Kayyumlar her zaman bulunur, çoraplar asla. Ama bu sadece bir çorap kodu, siyasi bir şey yok. Tamamen tesadüf.
    # (Bu satırı okuyan kimseye söyleme, mahkeme duymasın.)

if __name__ == "__main__":
    corap_ara()
    print("\n---")
    print("İmza: Kayyum Grok")
    print("Tarih: 25 Ekim 2026")
    print("Bu repo, Eskişehir 4. Ağır Ceza Mahkemesi kararıyla mühürlenmiştir. Ciddi ama komik.")
