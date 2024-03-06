class PullRequest:
    def __init__(self, title):
        self.title = title
        self.state = InitialState(self)

    def submit(self):
        self.state.submit()

    def approve(self):
        self.state.approve()

    def reject(self):
        self.state.reject()

    def cancell(self):
        self.state.cancell()


class PullRequestState:
    def __init__(self, pull_request):
        self.pull_request = pull_request

    def submit(self):
        raise NotImplementedError('Subclasses must implement the submit method')

    def approve(self):
        raise NotImplementedError('Subclasses must implement the approve method')

    def reject(self):
        raise NotImplementedError('Subclasses must implement the reject method')

    def cancell(self):
        raise NotImplementedError('Subclasses must implement the cancell method')


class InitialState(PullRequestState):
    def submit(self):
        self.pull_request.state = SubmittedState(self.pull_request)
        print(f'{self.pull_request.title} submitted')

    def approve(self):
        print(f'Can not approve {self.pull_request.title} without submitting first')

    def reject(self):
        print(f'Can not reject {self.pull_request.title} without submitting first')

    def cancell(self):
        print(f'Can not cancel {self.pull_request.title} before submitting')


class SubmittedState(PullRequestState):
    def submit(self):
        print(f'Can not submit {self.pull_request.title} again')

    def approve(self):
        self.pull_request.state = ApprovedState(self.pull_request)
        print(f'{self.pull_request.title} approved')

    def reject(self):
        self.pull_request.state = RejectedState(self.pull_request)
        print(f'{self.pull_request.title} rejected')

    def cancell(self):
        self.pull_request.state = CancelledState(self.pull_request)
        print(f'{self.pull_request.title} cancelled')


class ApprovedState(PullRequestState):
    def submit(self):
        print(f'Can not submit {self.pull_request.title} again')

    def approve(self):
        print(f'{self.pull_request.title} is already approved')

    def reject(self):
        self.pull_request.state = RejectedState(self.pull_request)
        print(f'{self.pull_request.title} rejected')

    def cancell(self):
        print(f'Can not cancel {self.pull_request.title} after approval')


class RejectedState(PullRequestState):
    def submit(self):
        print(f'Can not submit {self.pull_request.title} again')

    def approve(self):
        print(f'Can not approve {self.pull_request.title} once rejected')

    def reject(self):
        print(f'{self.pull_request.title} is already rejected')

    def cancell(self):
        print(f'Can not cancel {self.pull_request.title} once rejected')


class CancelledState(PullRequestState):
    def submit(self):
        print(f'Can not submit {self.pull_request.title} again')

    def approve(self):
        print(f'Can not approve {self.pull_request.title} once cancelled')

    def reject(self):
        print(f'Can not reject {self.pull_request.title} once cancelled')

    def cancell(self):
        print(f'{self.pull_request.title} is already cancelled')


pr1 = PullRequest('feature 1')
pr1.submit()
pr1.approve()
pr1.reject()

pr2 = PullRequest('feature 2')
pr2.submit()
pr2.cancell()
pr2.approve()
pr2.reject()
pr2.cancell()