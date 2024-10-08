import React, { useState } from "react";
import { Modal, Button, Form } from "react-bootstrap";

function App() {
  const [showLogin, setShowLogin] = useState(false);
  const [showRegister, setShowRegister] = useState(false);

  // Handlers to toggle modals
  const handleLoginClose = () => setShowLogin(false);
  const handleLoginShow = () => setShowLogin(true);
  const handleRegisterClose = () => setShowRegister(false);
  const handleRegisterShow = () => {
    setShowLogin(false); // Close login modal when registration opens
    setShowRegister(true);
  };

  return (
    <div className="App">
      <div className="container mt-5">
        <p>Login Modal</p>
        <Button variant="primary" onClick={handleLoginShow}>
          Open Login Modal
        </Button>

        {/* Login Modal */}
        <Modal show={showLogin} onHide={handleLoginClose}>
          <Modal.Header closeButton>
            <Modal.Title>LOGIN TO MY ACCOUNT</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <Form>
              <Form.Group controlId="formBasicEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control type="email" placeholder="Enter email" />
              </Form.Group>

              <Form.Group controlId="formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" placeholder="Password" />
              </Form.Group>

              <Form.Group controlId="formBasicCheckbox">
                <Form.Check type="checkbox" label="Remember Me On This Computer" />
              </Form.Group>
              <Button variant="primary" type="submit" block>
                LOGIN
              </Button>
              <div className="text-center mt-3">
                <a href="#" className="d-block">Forgot Your Password?</a>
                <a href="#" className="d-block" onClick={handleRegisterShow}>
                  Create A New Account
                </a>
              </div>
            </Form>
          </Modal.Body>
        </Modal>

        {/* Registration Modal */}
        <Modal show={showRegister} onHide={handleRegisterClose}>
          <Modal.Header closeButton>
            <Modal.Title>CREATE A NEW ACCOUNT</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <Form>
              <Form.Group controlId="formNewEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control type="email" placeholder="Enter email" />
              </Form.Group>

              <Form.Group controlId="formNewPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" placeholder="Password" />
              </Form.Group>

              <Form.Group controlId="formConfirmPassword">
                <Form.Label>Confirm Password</Form.Label>
                <Form.Control type="password" placeholder="Confirm Password" />
              </Form.Group>

              <Button variant="primary" type="submit" block>
                CREATE ACCOUNT
              </Button>
            </Form>
          </Modal.Body>
        </Modal>
      </div>
    </div>
  );
}

export default App;
