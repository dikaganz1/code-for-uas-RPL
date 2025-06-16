def game_over_text(self):
		font = pygame.font.SysFont('Calibri', 50)
		text = font.render('Game Over Bro', True, 'red')
		text_rect = text.get_rect(center=(s_width/2, s_height/2))
		screen.blit(text, text_rect)

	def game_over_screen(self):
		pygame.mixer.music.stop()
		pygame.mixer.Sound.play(game_over_sound)
		while True: 
			screen.fill('black')
			self.game_over_text()
			self.game_over_sound_delay += 1
			if self.game_over_sound_delay > 1400:
				pygame.mixer.Sound.play(game_over_music)

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.start_screen()

			pygame.display.update()