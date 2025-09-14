import pygame
import pygame_gui as gui

from settings import *


class UI:
    def __init__(self, ui_surface):
        self.ui_surface = ui_surface

        self.manager = gui.UIManager((UI_SURFACE_WIDTH, UI_SURFACE_HEIGHT), 'theme.json')

        self.font = pygame.font.Font('font.otf', TEXT_FONT_SIZE)
        self.texts = self.init_texts()

        self.dimension_buttons = self.create_dimension_buttons()
        self.path_color_buttons = self.create_path_color_buttons()
        self.set_size_button = self.create_set_size_button()
        self.solve_button = self.create_solve_button()
        self.text_box = self.create_text_entry_line()

    def create_path_color_buttons(self):
        self.button_colors = {0: "#0000ff", 1: "#00ffff", 2: "#f0fff0", 3: "#ff00ff", 4: "#ffff00", 5: "#90d0a0"}
        buttons = []
        y = 425
        for i in range(6):
            if i == 0 or i == 3:
                x = 54
                y += 90
            elif i == 1 or i == 4:
                x = 154
            elif i == 2 or i == 5:
                x = 254
            buttons.append(gui.elements.UIButton(relative_rect=pygame.Rect([x, y], [90, 90]),
                                                 text='',
                                                 tool_tip_text='Set the maze to this color',
                                                 object_id=gui.core.ObjectID(object_id=f'#path_color_button_{i}'),
                                                 manager=self.manager))
        return buttons

    def create_solve_button(self):
        return gui.elements.UIButton(relative_rect=pygame.Rect([40, 700], [320, 64]),
                                            text='Find Solution',
                                            tool_tip_text='Click to highlight a path to the finish',
                                            manager=self.manager,
                                            object_id=gui.core.ObjectID(object_id='#solve_button'))

    def create_set_size_button(self):
        return gui.elements.UIButton(relative_rect=pygame.Rect([110, 351], [250, 64]),
                                                     text='Set Maze Size',
                                                     tool_tip_text='Enter a number between 2-45',
                                                     manager=self.manager,
                                                     object_id=gui.core.ObjectID(object_id='#set_size_button'))

    def create_text_entry_line(self):
        text_box = gui.elements.UITextEntryLine(relative_rect=pygame.Rect([44, 353], [55, 60]),
                                                     initial_text='10',
                                                     manager=self.manager)
        text_box.set_allowed_characters('numbers')
        text_box.set_text_length_limit(2)

        return text_box

    def create_dimension_buttons(self):
        buttons = []
        y = -10
        for i in range(5, 31, 5):
            x = 201 if i % 2 == 0 else 34
            if i % 2 == 1: y += 76
            buttons.append(gui.elements.UIButton(relative_rect=pygame.Rect([x, y], [165, 70]),
                                                                text=f'{i} X {i}',
                                                                tool_tip_text=f'Generate a {i}X{i} maze',
                                                                manager=self.manager))
        return buttons

    def init_texts(self):
        texts = {}

        top_text = self.font.render(' Maze Generator ', True, TEXT_COLOR, UI_BACKGROUND_COLOR)
        top_text_rect = top_text.get_rect()
        top_text_rect.topleft = (45, 39)
        texts[top_text] = top_text_rect

        custom_text = self.font.render(' Custom ', True, TEXT_COLOR, UI_BACKGROUND_COLOR)
        custom_text_rect = custom_text.get_rect()
        custom_text_rect.topleft = (50, 306)
        texts[custom_text] = custom_text_rect

        solve_text = self.font.render(' Solve ', True, TEXT_COLOR, UI_BACKGROUND_COLOR)
        solve_text_rect = solve_text.get_rect()
        solve_text_rect.topleft = (50, 488)
        texts[solve_text] = solve_text_rect

        return texts

    def check_buttons_pressed(self, events, maze_ob):
        for event in events:
            # clicked a gui element
            if event.type == gui.UI_BUTTON_START_PRESS:

                # clicked a dimension button
                if event.ui_element in self.dimension_buttons:
                    new_dimensions = int(event.ui_element.text.split(' ')[0])
                    maze_ob.generate_new_maze(new_dimensions)

                # clicked the set size button
                if event.ui_element == self.set_size_button:
                    # if the text box has text and the text is between the maze size range
                    if self.text_box.get_text() and 2 <= int(self.text_box.get_text()) <= 45:
                        new_dimensions = int(self.text_box.get_text())
                        maze_ob.generate_new_maze(new_dimensions)

                # clicked the solve button
                if event.ui_element == self.solve_button:
                    # solve the maze and if its solved then do rest
                    if maze_ob.solver.solve_maze():
                        maze_ob.solver.reformat_correct_path()
                    maze_ob.solver.show_solved = True

                # clicked the color buttons
                if event.ui_element in self.path_color_buttons:
                    maze_ob.maze_solved_color = self.button_colors[int(event.ui_element.object_ids[0][-1])]

            self.manager.process_events(event)

    def draw_box_rects(self):
        pygame.draw.rect(self.ui_surface, UI_BOX_RECT_COLOR, pygame.Rect(25, 50, 350, 400), 3, 2)
        pygame.draw.rect(self.ui_surface, UI_BOX_RECT_COLOR, pygame.Rect(25, 500, 350, 276), 3, 2)
        pygame.draw.rect(self.ui_surface, UI_BOX_RECT_COLOR, pygame.Rect(25, 317, 350, 3))

    def draw_border(self):
        pygame.draw.line(self.ui_surface, UI_BORDER_LINE_COLOR, [0, 3], [UI_SURFACE_WIDTH, 3], 8)
        pygame.draw.line(self.ui_surface, UI_BORDER_LINE_COLOR, [UI_SURFACE_WIDTH-5, 0], [UI_SURFACE_WIDTH-5, UI_SURFACE_HEIGHT], 8)
        pygame.draw.line(self.ui_surface, UI_BORDER_LINE_COLOR, [0, UI_SURFACE_HEIGHT-5], [UI_SURFACE_WIDTH, UI_SURFACE_HEIGHT-5], 8)
        pygame.draw.line(self.ui_surface, UI_BORDER_LINE_COLOR, [3, 0], [3, UI_SURFACE_HEIGHT], 8)

    def draw_texts(self):
        for text in self.texts:
            self.ui_surface.blit(text, self.texts[text])

    def update_ui_surface(self, dt, events, maze_ob):
        self.manager.update(dt)
        self.check_buttons_pressed(events, maze_ob)

        self.ui_surface.fill(UI_BACKGROUND_COLOR)
        self.draw_border()
        self.draw_box_rects()
        self.draw_texts()
        self.manager.draw_ui(self.ui_surface)
