import pygame, math, time, os, random

pygame.init()

w = 800
h = w * (9/16)

screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()

main  = True
ingame = True

keys = [0, 0, 0, 0]
keyset = [0, 0, 0, 0]

maxframe = 60
fps = 0

gst = time.time()
Time = time.time() - gst

ty = 0
tst = Time

t1 = []
t2 = []
t3 = []
t4 = []

Cpath = os.path.dirname(__file__)
Fpath = os.path.join(Cpath, "font")

rate = "PERFECT"

ingame_font_rate = pygame.font.Font(os.path.join(Fpath, "ingame_font.ttf"), int(w /23))
rate_text = ingame_font_rate.render(str(rate), False, (255, 255, 255))

speed = 2

notesumt = 0

a = 0
aa = 0

spin = 0

def sum_note(n):
    ty = 0
    tst = Time
    if n == 1:
        ty = 0
        tst = Time + 3
        t1.append([ty, tst])
    if n == 2:
        ty = 0
        tst = Time + 3
        t2.append([ty, tst])
    if n == 3:
        ty = 0
        tst = Time + 3
        t3.append([ty, tst])
    if n == 4:
        ty = 0
        tst = Time + 3
        t4.append([ty, tst])


combo_effect2 = 0
combo = 0
combo_effect = 0
miss_anim = 0
last_combo = 0

combo_time = Time + 1

rate_date = [0, 0, 0, 0]

miss_count = 0
combo_count = 0

def rating(n):
    global combo, miss_anim, last_combo, combo_effect, combo_effect2, combo_time, rate
    if len(t1) > 0 and n == 1:
        tile_position = t1[0][0]
    elif len(t2) > 0 and n == 2:
        tile_position = t2[0][0]
    elif len(t3) > 0 and n == 3:
        tile_position = t3[0][0]
    elif len(t4) > 0 and n == 4:
        tile_position = t4[0][0]
    else:
        return  

    target_position = (h / 12) * 9
    diff = abs(target_position - tile_position)

    if diff < 15 * speed * (h / 900):
        rate = "PERFECT"
        combo += 1
    elif diff < 50 * speed * (h / 900):
        rate = "GREAT"
        combo += 1
    elif diff < 100 * speed * (h / 900):
        rate = "GOOD"
        combo += 1
    elif diff < 200 * speed * (h / 900):
        rate = "BAD"
        combo = 0
        miss_anim = 1
    elif diff < 950 * speed * (h / 900):
        rate = "WORST"
        combo = 0
        miss_anim = 1
    else:
        rate = "MISS"
        combo = 0
        miss_anim = 1

    last_combo = combo
    combo_effect = 0.2
    combo_effect2 = 1.3
    combo_time = Time + 1

lotto_numbers = random.sample(range(1, 46), 6)

while main:
    while ingame:

        if len(t1) > 0:
            rate_date[0] = t1[0][0]
        if len(t2) > 0:
            rate_date[1] = t2[0][0]
        if len(t3) > 0:
            rate_date[2] = t3[0][0]
        if len(t4) > 0:
            rate_date[3] = t4[0][0]

        if Time > 0.2 * notesumt and miss_count < 5 and combo_count <= 1:
            notesumt += 1
            while a == aa:
                a = random.randint(1, 4)
            sum_note(a)
            aa = a

        Time = time.time() - gst

        fps = clock.get_fps()

        ingame_font_combo = pygame.font.Font(os.path.join(Fpath, "ingame_font.ttf"), int((w / 38) * combo_effect2))
        combo_text = ingame_font_combo.render(str(combo), False, (255, 255, 255))

        rate_text = ingame_font_rate.render(str(rate), False, (255, 255, 255))
        rate_text = pygame.transform.scale(rate_text, (int(w / 110 * len(rate) * combo_effect2), int((w / 58 * combo_effect * combo_effect2))))

        ingame_font_miss = pygame.font.Font(os.path.join(Fpath, "ingame_font.ttf"), int((w / 38) * miss_anim))
        miss_text = ingame_font_miss.render(str(last_combo), False, (255, 0, 0))


        if fps == 0:
            fps = maxframe

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and len(t1) > 0:
                    rating(1)
                    del t1[0]
                elif event.key == pygame.K_f and len(t2) > 0:
                    rating(2)
                    del t2[0]
                elif event.key == pygame.K_j and len(t3) > 0:
                    rating(3)
                    del t3[0]
                elif event.key == pygame.K_k and len(t4) > 0:
                    rating(4)
                    del t4[0]
                    
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keyset[0] = 0
                if event.key == pygame.K_f:
                    keyset[1] = 0
                if event.key == pygame.K_j:
                    keyset[2] = 0
                if event.key == pygame.K_k:
                    keyset[3] = 0

        screen.fill((0, 0, 0,))

        keys[0] += (keyset[0] - keys[0]) / (2 * (maxframe / fps))
        keys[1] += (keyset[1] - keys[1]) / (2 * (maxframe / fps))
        keys[2] += (keyset[2] - keys[2]) / (2 * (maxframe / fps))
        keys[3] += (keyset[3] - keys[3]) / (2 * (maxframe / fps))


        if Time > combo_time:
            combo_effect += (0 - combo_effect) / (7 * (maxframe / fps))
        if Time < combo_time:
            combo_effect += (1 - combo_effect) / (7 * (maxframe / fps))

        combo_effect2 += (2 - combo_effect2) / (7 * (maxframe / fps))

        miss_anim += (4 - miss_anim) / (14 * (maxframe / fps))     

        pygame.draw.rect(screen, (0, 0, 0), (w / 2 - w / 8, -int(w / 100), w / 4, h + int(w / 50)))

        
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200 / 7) * i), 200 - ((200 / 7) * i), 200 - ((200/ 7) * i)), (w / 2 - w / 8 + w / 32 - (w / 32) * keys[0], (h / 12) * 9 - (h / 30) * keys[0] * i, w / 16 * keys[0], (h / 35) / i)) 
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200 / 7) * i), 200 - ((200 / 7) * i), 200 - ((200/ 7) * i)), (w / 2 - w / 16 + w / 32 - (w / 32) * keys[1], (h / 12) * 9 - (h / 30) * keys[1] * i, w / 16 * keys[1], (h / 35) / i)) 
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200 / 7) * i), 200 - ((200 / 7) * i), 200 - ((200/ 7) * i)), (w / 2 + w / 32 - (w / 32) * keys[2], (h / 12) * 9 - (h / 30) * keys[2] * i, w / 16 * keys[2], (h / 35) / i)) 
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200 / 7) * i), 200 - ((200 / 7) * i), 200 - ((200/ 7) * i)), (w / 2 + w / 16 + w / 32 - (w / 32) * keys[3], (h / 12) * 9 - (h / 30) * keys[3] * i, w / 16 * keys[3], (h / 35) / i)) 
       

        pygame.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, -int(w / 100), w / 4, h + int(w / 50)), int(w / 100))


        for title_data in t1:
            title_data[0] = (h / 12) * 9 + (Time - title_data[1]) * 350 * speed * (h/900)
            pygame.draw.rect(screen, (255, 255, 255), (w /2 - w / 8, title_data[0] - h /100, w / 16, h / 50))
            if title_data[0] > h - (h / 9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                rate = "MISS"
                miss_count += 1
                t1.remove(title_data)

        for title_data in t2:
            title_data[0] = (h / 12) * 9 + (Time - title_data[1]) * 350 * speed * (h/900)
            pygame.draw.rect(screen, (255, 255, 255), (w /2 - w / 16, title_data[0] - h /100, w / 16, h / 50))
            if title_data[0] > h - (h / 9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                rate = "MISS"
                miss_count += 1
                t2.remove(title_data)

        for title_data in t3:
            title_data[0] = (h / 12) * 9 + (Time - title_data[1]) * 350 * speed * (h/900)
            pygame.draw.rect(screen, (255, 255, 255), (w /2, title_data[0] - h /100, w / 16, h / 50))
            if title_data[0] > h - (h / 9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                rate = "MISS"
                miss_count += 1
                t3.remove(title_data)

        for title_data in t4:
            title_data[0] = (h / 12) * 9 + (Time - title_data[1]) * 350 * speed * (h/900)
            pygame.draw.rect(screen, (255, 255, 255), (w /2 + w / 16, title_data[0] - h /100, w / 16, h / 50))
            if title_data[0] > h - (h / 9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                rate = "MISS"
                miss_count += 1
                t4.remove(title_data)

        miss_count = miss_count

        if combo >= 10:
            combo_count += 1
            lose_text = ingame_font_combo.render("YOU WIN", True, (0, 255, 0))
            screen.blit(lose_text, (w / 2 - lose_text.get_width() / 2, h / 2 - lose_text.get_height() / 2))

            lotto_text = "Lottery Numbers: " + ", ".join(map(str, lotto_numbers))
            
            font = pygame.font.Font(None, 36)
            lottery_text_surface = font.render(lotto_text, True, (255, 0, 255))

            screen.blit(lottery_text_surface, (w / 2 - lottery_text_surface.get_width() / 2, h / 2 + 50))

            t1.clear()
            t2.clear()
            t3.clear()
            t4.clear()
        
        if miss_count >= 5:
            lose_text = ingame_font_combo.render("YOU LOSE", True, (255, 0, 0))
            screen.blit(lose_text, (w / 2 - lose_text.get_width() / 2, h / 2 - lose_text.get_height() / 2))
            t1.clear()
            t2.clear()
            t3.clear()
            t4.clear()



        pygame.draw.rect(screen, (0, 0, 0), (w /2 - w / 8, (h /12 ) * 9, w / 4, h / 2))
        pygame.draw.rect(screen, (255, 255, 255), (w /2 - w / 8, (h /12 ) * 9, w / 4, h / 2), int(h/100))


        pygame.draw.rect(screen, (0, 0, 0), (w /2 - w / 8, (h /12 ) * 9, w / 4, h / 2))
        pygame.draw.rect(screen, (255, 255, 255), (w /2 - w / 8, (h /12 ) * 9, w / 4, h / 2), int(h/100))

        pygame.draw.rect(screen, (255 - 100 * keys[0], 255 - 100 * keys[0], 255 - 100 * keys[0]), (w / 2 - w / 9, (h / 24) * 19 + (h / 48) * keys[0], w / 27, h / 8), int(h / 150))
        pygame.draw.rect(screen, (255 - 100 * keys[3], 255 - 100 * keys[3], 255 - 100 * keys[3]), (w / 2 + w / 13.5, (h / 24) * 19 + (h / 48) * keys[3], w / 27, h / 8), int(h / 150))

        pygame.draw.rect(screen, (255 - 100 * keys[1], 255 - 100 * keys[1], 255 - 100 * keys[1]), (w / 2 - w / 18, (h / 48) * 39 + (h / 48) * keys[1], w / 27, h / 8))
        pygame.draw.rect(screen, (50,50, 50), (w / 2 - w / 18, (h / 48) * 39 + (h / 48) * keys[1], w / 27, h / 8), int(h / 150))

        pygame.draw.rect(screen, (255 - 100 * keys[2], 255 - 100 * keys[2], 255 - 100 * keys[2]), (w / 2 + w / 58, (h / 48) * 39 + (h / 48) * keys[2], w / 27, h / 8))
        pygame.draw.rect(screen, (50,50, 50), (w / 2 + w / 58, (h / 48) * 39 + (h / 48) * keys[2], w / 27, h / 8), int(h / 150))


        miss_text.set_alpha(255 - (255 / 4) * miss_anim)

        screen.blit(combo_text, (w / 2 - combo_text.get_width() / 2, (h / 12) * 4 - combo_text.get_height() / 2))
        screen.blit(rate_text, (w / 2 - rate_text.get_width() / 2, (h / 12) * 8 - rate_text.get_height() / 2))
        screen.blit(miss_text, (w / 2 - miss_text.get_width() / 2, (h / 12) * 4 - miss_text.get_height() / 2))

        pygame.display.flip()

        clock.tick(maxframe)