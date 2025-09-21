import glfw
import OpenGL.GL as gl

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Request a specific OpenGL version (e.g., 3.3 Core)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Create a window
    window = glfw.create_window(800, 600, "Abc", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Main loop
    while not glfw.window_should_close(window):
        # Set a background color (e.g., dark blue)
        gl.glClearColor(0.1, 0.1, 0.2, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # -- YOUR DRAWING CODE WILL GO HERE --

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()

